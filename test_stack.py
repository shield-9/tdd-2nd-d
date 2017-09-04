import unittest
from stack import Stack, EmptyStackException


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_create(self):
        self.assertTrue(self.stack.isEmpty())

    def test_PushAndTop(self):
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())
        self.assertEqual(1, self.stack.top())
    
    def test_PushAndSize(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.size())
        self.stack.push(2)
        self.assertEqual(2, self.stack.size())

    def test_EmptyPop(self): 
        self.assertRaises(EmptyStackException, self.stack.pop)

    def test_EmptyTop(self):
        self.assertRaises(EmptyStackException, self.stack.top)

    def test_PushAndPop(self):
        self.stack.push(1)
        self.stack.pop()
        self.assertEqual(0, self.stack.size())


    # def test_isEmpty(self):
    #     pass

    # def test_size(self):
    #     pass

    # def test_push(self):
    #     pass

    # def test_pop(self):
    #     pass

    # def test_top(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
