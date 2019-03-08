# scaledarcherytargets
A python script to generate scaled archery targets.

There is no validation of user input currently, have fun with that.


useage scaledArcheryTarget.py [-dowrlvcntxh]

	-d <diameter>		: Diameter in mm, defaults to 400mm if unspecified
	-o <output file>	: File Name, defaults to target-diameter.  Will have .svg appended automatically
	-w <line width>		: Line Width, defaults to diameter/1000 max 1mm
	-r <number of targets>	: A vertical row of targets, creates a block of targets when specified with -l
	-l <number of targets>	: a horizontal line of targets, creates a block of targets when specified with -r
	-v			: Vegas Style Triangular Target, best used with Target Centers
	-c			: Target Center Only
	-n			: Print Numbers for scoring
	-t			: Omit Ten ring (for indoor compound targets)
	-x			: Omit X ring (for indoor recurve targets)
	-h			: Print Useage Information


