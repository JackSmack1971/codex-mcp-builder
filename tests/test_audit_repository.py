import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_repository import inventory, compare, git_state

class AuditTests(unittest.TestCase):
    def test_inventory_deterministic_and_detects_edits(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'a.txt').write_text('one')
            before = inventory(root)
            self.assertEqual(before, inventory(root))
            (root/'a.txt').write_text('two')
            self.assertEqual(compare(before, inventory(root), set())['outside_expected_scope'], ['a.txt'])
            self.assertEqual(compare(before, inventory(root), {'a.txt'})['outside_expected_scope'], [])

    def test_untracked_addition_and_deletion_detected(self):
        self.assertEqual(compare({'gone':'x'}, {'new':'y'}, set())['changed'], ['gone','new'])

    def test_gitless_does_not_invent_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertFalse(git_state(Path(tmp))['available'])

if __name__ == '__main__': unittest.main()
