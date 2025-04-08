class OnBoardComputer:

    def get_next_burn(self, status):
        seconds = status.get_tick()
        burn = 200
        # when time is under 80 seconds burn fuel for 200

        # when time is between 150 and 90 seconds

        # burn cannot be less than 100 and greater than 150

        # when time is 160 seconds burn must be less than 120 but greater than 100
        if seconds <= 80:
            burn = 200
        elif 90 <= seconds <= 150:
            burn = 125
        elif seconds >= 160:
            burn = 110

        print(burn)
        return burn

#burn = OnBoardComputer.get_next_burn()
