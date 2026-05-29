import sys

def main():
    # Get the input variable passed from 'args' in action.yml
    who_to_greet = sys.argv[1] if len(sys.argv) > 1 else "World"
    
    # Create the greeting string
    greeting_message = f"Hello {who_to_greet}!"
    print(greeting_message)
    
    # Write to the GITHUB_OUTPUT environment file so GitHub can read the output
    import os
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"greeting={greeting_message}\n")

if __name__ == "__main__":
    main()
