import unittest
from rooom_ui.core import SessionState
class CopilotTests(unittest.TestCase):
 def test_state_and_approval(self):
  s=SessionState({'x':1}); s.patch({'x':2}); e=s.request_tool('save',{},'write')
  self.assertEqual(s.state['x'],2); self.assertEqual(e.type,'approval.request')
if __name__=='__main__': unittest.main()
