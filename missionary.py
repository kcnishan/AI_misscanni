



from State import *
import sys


def breadth_first_search():
    initial_state = State(3, 3, 'left', 0, 0)
    if initial_state.final():
        return initial_state
    unexploCOLOR2valid = list()
    exploCOLOR2 = set()
    unexploCOLOR2valid.append(initial_state)
    while unexploCOLOR2valid:
        state = unexploCOLOR2valid.pop(0)
        if state.final():
            return state
        exploCOLOR2.add(state)
        child = childstate(state)
        for child in child:
            if (child not in exploCOLOR2) or (child not in unexploCOLOR2valid):
                unexploCOLOR2valid.append(child)

    return None


def main():
    pygame.init()

    # Define some colors
    COLOR1 = (10, 20, 100)
    COLOR2 = (100, 20, 10)

    pygame.display.set_caption("Missionaries_Cannibals:AI assignment")

    # Set positions of graphics
    bg_position = [0, 0]
    carrierleft_position = [110, 190]
    carrierright_position = [450, 300]

    # Loop until the user clicks the close button.
    click = False
    clock = pygame.time.Clock()
    # Loop as long as click == False
    while not click:
        solution = breadth_first_search()
        path = []
        path.append(solution)
        parent = solution.parent
        while parent:
            path.append(parent)
            parent = parent.parent

        for i in path:
             print(i.left_canni, i.left_missi, i.right_canni, i.right_missi)
        s = []
        r = []
        id = 0;
        s.append(id)
        r.append(id)
        state = path[len(path) - 1]

        s[id] = Node("(" + str(state.left_canni) + "," + str(state.left_missi) \
                     + "," + state.turtle + "," + str(state.right_canni) + "," + \
                     str(state.right_missi) + ")")
        r[id] = Node("(" + str(state.left_canni) + "," + str(state.left_missi) \
                     + "," + state.turtle + "," + str(state.right_canni) + "," + \
                     str(state.right_missi) + ")")

        for t in range(len(path)):

            state = path[len(path) - t - 1]

            if state.turtle == 'left':
                screen.blit(carrier, carrierleft_position)

            if state.turtle == 'right':
                screen.blit(carrier, carrierright_position)

            if state.left_canni > 0:
                for i in range(1, state.left_canni + 1):
                    pygame.draw.line(screen, COLOR1, [i * 1, 10], [i * 1, 100], 2)
                    screen.blit(canni, (i * 20, 150 + (i * 10)))

            if state.right_canni > 0:
                for j in range(1, state.right_canni + 1):
                    pygame.draw.line(screen, COLOR1, [500 + (j * 10), 0], [500 + (j * 10), 100], 2)
                    screen.blit(canni, [500 + (j * 20), 350 + (j * 40)])

            if state.left_missi > 0:
                for i in range(1, state.left_missi + 1):
                    pygame.draw.line(screen, COLOR2, [i * 10 + 30, 0], [i * 10 + 30, 100], 2)
                    screen.blit(missi, [(i * 20) + 50, 20 + (i * 41)])

            if state.right_missi > 0:
                for j in range(1, state.right_missi + 1):
                    pygame.draw.line(screen, COLOR2, [500 + (j * 10) + 30, 0], [500 + (j * 10) + 30, 100], 2)
                    screen.blit(missi, [520 + (j * 20), 300 + (j * 40)])


            screen.blit(background_image, bg_position)

            for f in range(0, id + 1):

                a = Node("(" + str(state.left_canni) + "," + str(state.left_missi) \
                         + "," + state.turtle + "," + str(state.right_canni) + "," + \
                         str(state.right_missi) + ")")

                if r[f].name == a.name:
                    root = f
            for p in range(len(state.child)):
                states = state.child[len(state.child) - p - 1]
                id = id + 1

                if state.turtle == 'left':
                    # pygame.draw.rect(screen, COLOR2, [70, 20, 100, 50], 2)
                    screen.blit(carrier, carrierleft_position)

                if state.turtle == 'right':
                    # pygame.draw.rect(screen, COLOR2, [400, 20,100, 50], 2)
                    screen.blit(carrier, carrierright_position)

                if state.left_canni > 0:
                    for i in range(1, state.left_canni + 1):
                        pygame.draw.line(screen, COLOR1, [i * 10, 0], [i * 10, 100], 2)
                        screen.blit(canni, (i * 20, 30 + (i * 20)))

                if state.right_canni > 0:
                    for j in range(1, state.right_canni + 1):
                        pygame.draw.line(screen, COLOR1, [500 + (j * 10), 0], [500 + (j * 10), 100], 2)
                        screen.blit(canni, [450 + (j * 20), 350 + (j * 40)])

                if state.left_missi > 0:
                    for i in range(1, state.left_missi + 1):
                        pygame.draw.line(screen, COLOR2, [i * 10 + 30, 0], [i * 10 + 30, 100], 2)
                        screen.blit(missi, [i * 20 + 150, 75 + (i * 20)])

                if state.right_missi > 0:
                    for j in range(1, state.right_missi + 1):
                        pygame.draw.line(screen, COLOR2, [500 + (j * 10) + 30, 0], [500 + (j * 10) + 30, 100], 2)
                        screen.blit(missi, [520 + (j * 20), 300 + (j * 40)])
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                # update the screen
                pygame.display.update()
                pygame.time.delay(1000)


                # Copy image to screen:
                screen.blit(background_image, bg_position)

                s.append(id)
                r.append(id)
                s[id] = Node("(" + str(states.left_canni) + "," + str(states.left_missi) \
                             + "," + states.turtle + "," + str(states.right_canni) + "," + \
                             str(states.right_missi) + ")", parent=s[root])
                r[id] = Node("(" + str(states.left_canni) + "," + str(states.left_missi) \
                             + "," + states.turtle + "," + str(states.right_canni) + "," + \
                             str(states.right_missi) + ")")

        for pre, fill, node in RenderTree(s[0]):
            print("%s%s" % (pre, node.name))

        for j in range(1, 4):
            pygame.draw.line(screen, COLOR2, [500 + (j * 10) + 30, 0], [500 + (j * 10) + 30, 100], 2)
            screen.blit(missi, [520 + (j * 20), 300 + (j * 40)])

        for i in range(1, 4):
            pygame.draw.line(screen, COLOR1, [500 + (i * 10), 0], [500 + (i * 10), 100], 2)
            screen.blit(canni, [420 + (i * 20), 250 + (i * 40)])

        font = pygame.font.SysFont("comicsansms", 50)
        text = font.render(" MISSION ACCOMPLISHED!!", True, (10, 10, 10))
        screen.blit(text,
                    (350 - text.get_width() // 2, 200 - text.get_height() // 2))
        pygame.display.flip()

        clock.tick()
        pygame.quit()


# if called from the command line, call main()
if __name__ == "__main__":
    main()




