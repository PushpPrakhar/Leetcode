from dataclasses import dataclass
@dataclass
class Robot:
  index: int
  position: int
  health: int
  direction: str

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted([Robot(index, position, health, direction)
                     for index, (position, health, direction) in
                     enumerate(zip(positions, healths, directions))],
                    key=lambda robot: robot.position)
        # using stack to perform the operation
        stack: List[Robot] = []

        #adding the robots with diretion = R to the stack
        for robot in robots:
            if robot.direction == 'R':
                stack.append(robot)
                continue
            #collide with robots going right is any
            while stack and stack[-1].direction == 'R' and robot.health > 0:
                #if they both have the same health
                if stack[-1].health == robot.health:
                    stack.pop()
                    robot.health = 0
                #if the health of the robot is greater
                elif stack[-1].health < robot.health:
                    stack.pop()
                    robot.health -= 1
                #if the health of previous robot is greater
                else:  # stack[-1].health > robot.health
                    stack[-1].health -= 1
                    robot.health = 0
            if robot.health > 0:
                stack.append(robot)

        stack.sort(key=lambda robot: robot.index)
        return [robot.health for robot in stack]

