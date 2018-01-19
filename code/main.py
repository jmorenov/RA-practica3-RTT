import rrt_planning
import map1 as map

show_animation = True

def main():
    print("start RRT path planning")
    rrt = rrt_planning.RRT(start=map.start, goal=map.goal,
              randArea=map.randArea, obstacleList=map.obstacleList)
    path = rrt.Planning(animation=show_animation)

    # Draw final path
    if show_animation:
        rrt.DrawFinalGraph(path)

if __name__ == '__main__':
    main()