from somewhere_deep_in_an_external_package import Line, Plot


def draw(p: Plot):
    p.draw()
    return


def get_l_from_p(p: Plot) -> Line:
    result: Line = p.L[0]  # type: ignore
    return result
