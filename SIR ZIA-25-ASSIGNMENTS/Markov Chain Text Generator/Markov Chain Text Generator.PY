import random
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.chain = defaultdict(list)
    
    def train(self, text, order=2):
        words = text.split()
        for i in range(len(words) - order):
            state = tuple(words[i:i + order])
            next_word = words[i + order]
            self.chain[state].append(next_word)
    
    def generate(self, length=50, order=2):
        if not self.chain:
            return "No training data provided"
        
        current_state = random.choice(list(self.chain.keys()))
        result = list(current_state)
        
        for _ in range(length - order):
            possible_words = self.chain.get(current_state, [])
            if not possible_words:
                break
            
            next_word = random.choice(possible_words)
            result.append(next_word)
            current_state = tuple(result[-order:])
        
        return ' '.join(result)

def main():
    print("Markov Chain Text Generator")
    
    # Sample training text
    sample_text = """This is a sample text. It shows how the Markov chain 
    works. The chain generates new text based on patterns in this input."""
    
    mc = MarkovChain()
    mc.train(sample_text)
    
    while True:
        print("\nOptions:")
        print("1. Generate text")
        print("2. Train with new text")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            length = int(input("Enter output length (words): "))
            print("\nGenerated text:")
            print(mc.generate(length))
            
        elif choice == "2":
            new_text = input("Enter training text: ")
            mc.train(new_text)
            print("Text trained successfully")
            
        elif choice == "3":
            print("Exiting program")
            break
            
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()