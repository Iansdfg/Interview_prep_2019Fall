class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.is_word = False


class Solution:
    def __init__(self):
        self.root = TrieNode('')


    def insert(self, word):
        curr_node = self.root
        val = ''

        for char in word:
            val += char
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode(val)
            curr_node = curr_node.children[char]
        
        curr_node.is_word = True

    def search_by_prefix(self, prefix):
        curr_node = self.root

        for char in prefix:
            if char not in curr_node.children:
                return []
            curr_node = curr_node.children[char]
        words = self.get_word(curr_node)
        words.sort()
        return words if len(words) <= 3 else words[:3]

    def get_word(self, node):
        stack = [node]
        res = []
        while stack:
            curr = stack.pop()

            if curr.is_word:
                res.append(curr.val)
            for child in curr.children.values():
                stack.append(child)
        return res


    def product_suggestions(self, products, query):
        if len(query) <= 1 or not products:
            return None

        for product in products:
            self.insert(product)

        input_queries = []

        for i in range(2, len(query)+1):
            input_queries.append(query[:i])

        results = []
        for input_query in input_queries:
            result = self.search_by_prefix(input_query)
            results.append(result)

        return results

        
if __name__ == "__main__":
    test = Solution()
    products1 = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    query1 = "mouse"
    products2 = ["ps4", "ps4 slim", "ps4 pro", "xbox", "tissue",
                    "standing table", "house", "true love", "tracking device"]
    query2 = "ps4"
    query21 = "tru"
    query22 = "t"
    print('case1', test.product_suggestions(products1, query1))
    print('case2',test.product_suggestions(products2, query2))
    print('case3',test.product_suggestions(products2, query21))
    print('case4',test.product_suggestions(products2, query22))
