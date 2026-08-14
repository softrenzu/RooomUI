from __future__ import annotations

import copy
import uuid
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True, slots=True)
class Event:
    id: str
    type: str
    payload: dict[str,Any]

class SessionState:
    def __init__(self,initial:dict[str,Any]|None=None): self._state=copy.deepcopy(initial or {}); self._events=[]
    @property
    def state(self)->dict[str,Any]: return copy.deepcopy(self._state)
    def patch(self,changes:dict[str,Any])->Event:
        for k,v in changes.items():
            if v is None: self._state.pop(k,None)
            else: self._state[k]=copy.deepcopy(v)
        return self.emit('state.patch',{'changes':copy.deepcopy(changes)})
    def emit(self,event_type:str,payload:dict[str,Any])->Event:
        if event_type not in {'state.patch','ui.render','tool.request','tool.result','approval.request','approval.result','message'}:
            raise ValueError('unsupported event type')
        event=Event(uuid.uuid4().hex,event_type,copy.deepcopy(payload)); self._events.append(event); return event
    def request_tool(self,name:str,args:dict[str,Any],risk:str='read')->Event:
        if risk not in {'read','write','external'}: raise ValueError('invalid risk')
        typ='tool.request' if risk=='read' else 'approval.request'
        return self.emit(typ,{'tool':name,'arguments':copy.deepcopy(args),'risk':risk})
    def events(self,since:int=0)->list[Event]: return list(self._events[max(0,since):])
