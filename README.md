# ASSIGNMENT Solution
**Installing Package:**<br>
On Terminal Run:<br>
`colcon build`<br>
If it gives error like `stderror`.
In `src/assignment_1/setup.py` Comment out 15th line.
<br>
<br>
**Teleporting the Turtle:**<br>
On Terminal Run:<br>
``ros2 launch assignment_1 q1launch.py x,y,theta:=<x>,<y>,<theta>``
<br>
<br>
**Circular Trajectory:**<br>
On Terminal Run:<br>
``ros2 launch assignment_1 q2launch.py r,s:=<r>,<s>``
<br>
<br>
If launch command doesn't work move to `src/assignment_1/launch` and run:<br>
`ros2 launch <launchfile.py> <parameters>`