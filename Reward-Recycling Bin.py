  # Reward-Recycling Bin Stimulation

RECYCLABLE_ITEMS = {"paper", "plastic bottle", "glass bottle", "aluminum can", "cardboard", "tin can"}
NON_RECYCLABLE_ITEMS = {"food waste", "styrofoam", "diaper", "plastic bag", "ceramic", "broken mirror"}

POINTS_CORRECT =10
POINTS_WRONG = -5

class RecyclingBin:
    def __init__(self):
        self.points = 0
        
    def detect_item(self, item):
        item = item.lower().strip()
        if item in RECYCLABLE_ITEMS:
            return "recyclable"
        elif item in NON_RECYCLABLE_ITEMS:
            return "non-recyclable"
        else:
            return "unknown"
        
    def process_item(self, item):
        item_type = self.detect_item(item)
        if item_type == "recyclable":
            self.points += POINTS_CORRECT
            print(f"'{item}' is recyclable. +{POINTS_CORRECT} points!")
        elif item_type == "non-recyclable":
            self.points += POINTS_WRONG
            print(f"'{item}' is not recyclable. {POINTS_WRONG} points.")
        else:
            print(f"Unknown item '{item}'. No points awarded or deducted.")
            
        print(f"Current Points: {self.points}\n")
        
def main():
    bin = RecyclingBin()
    print("Welcome to the Reward Recycling Bin!")
    print("Type 'exit' to stop.\n")
        
    while True:
        item = input("Throw an item into the recycling bin: ")
        if item.lower() == 'exit':
                print(f"Session ended. Total Points: {bin.points}")
                break
        bin.process_item(item)
            
if __name__ == "__main__":
        main()
        