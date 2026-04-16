class Solution:
    def simplifyPath(self, path: str) -> str:
        options = {
            '.': 'NOTHING',
            '..': 'POP STACK'
        }

        stack = []
        path = path.split('/')

        for directory in path:
            if not directory:
                continue

            if directory == '..':
                if stack:
                    stack.pop()
            elif not directory.replace('.', ''):
                stack.append(directory)
            else:
                stack.append(directory)

        return '/' + '/'.join(stack)