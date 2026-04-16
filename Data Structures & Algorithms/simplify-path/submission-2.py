class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')

        for directory in path:
            if not directory:
                continue

            if directory == '..':
                if stack:
                    stack.pop()
            elif directory.replace('.', '').strip():
                stack.append(directory)
            elif directory == '.':
                continue
            else:
                stack.append(directory)

        return '/' + '/'.join(stack)