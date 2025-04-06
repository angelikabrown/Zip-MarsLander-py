from turtledemo.clock import tick

from marslander.DescentEvent import DescentEvent


class BurnInputStream:
    def get_next_burn(self, status):
        while True:
            try:
                tokens = input().split()
                if tokens:
                    burn = int(tokens[0])
                    return burn
            except ValueError:
                print("Must Enter a Number (0-200)")

# Example usage:
# burn_input_stream = BurnInputStream()
# status = DescentEvent()
# burn = burn_input_stream.get_next_burn(status)
# print(burn)
