The idea of this project is to allow Beat Saber players to input their profiles and receive song recommendations based on difficulty.
In order to do this, I leveraged the Scoresaber API to get data on the player's top scores, using the average difficulty of these scores to set the minimum
and maximum difficulty. The next query uses this difficulty range as well as a couple of other filters to fetch the most popular songs within the difficulty range.

The end result is a list of songs that the user can then use to inform them of songs that could be within their reach with respect to skill.

The next steps are:
- Filtering out songs the user has already completed
- Creating a GUI or webpage
- Allowing the user to download songs directly from the page or GUI
