DEPENDANCIES
============

 Python 2.5.4  -  http://www.python.org/
 PyGame 1.9.1  -  http://www.pygame.org/

INSTRUCTIONS
============

To use the level-edit system, 4 things are needed in a single text file

1. The first line will be the text displayed at the start of the level
2. The last line will be the name of the music (.mp3) file played during
	the level. Note that the music file must be placed in the "data" folder,
	or it will not play. Also note that entering garbage text will not crash
	the game, instead no music will be played.
		NOTE: The music will loop upon finishing.
3. The center portion must consist of alternating numbers and characters on
	lines. The numbers are 1/2 seconds, and the letters correspond to the
	following:
	w -> normal black wall
	b -> flashing "bomb" wall
	3w-> 3 consecutive normal walls
	g -> generator (first boss)
	k -> special black wall; ends the level, but is otherwise identical to
			the normal black wall.
	f -> unused, but accepted character, will call the final boss on final
			release of Shifter.
	
	EXAMPLE SCRIPT (LEVEL1.txt):
	============================
	LEVEL 1
	4
	w
	5
	3w
	10
	g
	243860_03_What_did_you_say.mp3
	===============
	as you can see in the above script, the text "LEVEL 1" will be displayed
	when the level starts. At 2 seconds a single black wall will appear. At
	2.5 seconds, 3 consecutive walls will appear, and at 5 seconds, the boss
	Generator will be summoned. After killing the Generator, the level will
	end and the game will then search for a file called "LEVEL2.txt". If the
	file does not exist, the gameplay will end and the credits will roll.
	
	NOTE: The file "LEVEL1.txt" MUST exist or the game may crash. Any
		consecutive levels can be included, if they are named as follows:
		"LEVEL2.txt", "LEVEL3.txt", "LEVEL4.txt", ..., and so on.

LICENSE
=======

SHIFTER - A Video Game by Michael Arevalo
Copyright (C) 2010


This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA