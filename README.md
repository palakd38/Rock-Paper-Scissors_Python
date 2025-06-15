# Rock-Paper-Scissors
This is an implementation of the popular Rock-Paper-Scissors game in Python. The game consists of two variants, one is the classic version and the second one is an extended version with Spock and Lizard. The game supports a human player and a computer player.

The Game is programmed in such a way that it is extandable and new variants can be added easily without changing the Game logic. It uses a common Interface Ruleset, using Strategy pattern, applicable to all the variants.  

Hence, the game remains expandable for future rule variants by using a well-defined RuleSet interface, allowing new rule sets to be added without changing existing code. By following the strategy pattern, each variant implements the same methods (get_choices, get_winner, and get_name), for easier integration with the game engine. 
