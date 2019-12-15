# S-Code

S-code describes a set of codes used to communicate with a SMARS robot.

An example sent over bluetooth would be:

```python
S111 3
```

This would move the robot forward 3 units. A unit is dependent on lots of things so its hard to define in the language.

## Generic Movement

```python
100 - # Movement
101 - Move Forward
102 - Move backward
103 - Turn left
104 - Turn right
```

## Wheeled SMARS

 ```python
 110 - # Movement
 111 - Move Forward
 112 - Move Backwards
 113 - Turn Left
 114 - Turn Right
```

## Quad Smars

 ```python
 150 - # Quad SMARS movements
 151 - Walk Forward
 152 - Walk Backward
 153 - Turn Left
 154 - Turn Right
 155 - Stand Up
 156 - Sit Down
 157 - Clap
 158 - Wiggle
```

## Inputs

```python
200 - # Inputs, sensors
210 - Light sensor
211 - get light level
220 - Line sensor
221 - get light level
230 - Ultrasonic sensor
231 - get distance from sensor
240 - # Battery Level
241 - get battery level
250 - # IMU
251 - Get position from IMU
252 - Get Compass Heading
```

## Outputs

```python
300 - # output - sound and lights
400 - status
401 - get current status
500 - Other Motors (for future use)
501 - Move motor 1
```
