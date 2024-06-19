import math

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

import diagram_style
import cooperation_data
from cooperation_data import Department, Institution

def drawLegendRect(ax, pos, color, text, style):
    ax.add_patch(plt.Rectangle(pos, style.legendRectsize, style.legendRectsize, fc=color))
    ax.text(pos[0] + style.legendSpace, pos[1] + style.legendRectsize2, text, size=style.legendFontSize, ha="left", va="center")

def departmentToColor(department, style):
    match department:
        case Department.geo:
            return style.geoColor
        case Department.bio:
            return style.bioColor
        case Department.comp:
            return style.compColor
        case _:
            print(f"Unknown department: {fc}")
            return "black"

def drawCircle(ax, pos, lw, fc, ec, style):
    if isinstance(fc, str):
        ax.add_patch(plt.Circle(pos, style.legendRectsize2, lw=lw, fc=fc, ec=ec))
    elif isinstance(fc, list):
        match len(fc):
            case 1:
                color = departmentToColor(fc[0], style)
                ax.add_patch(plt.Circle(pos, style.legendRectsize2, lw=lw, fc=color, ec=ec))

            case 2:
                (dp1, amount1) = fc[0]
                (dp2, amount2) = fc[1]
                color1 = departmentToColor(dp1, style)
                color2 = departmentToColor(dp2, style)
                t1 = 0
                t2 = 360

                match (amount1, amount2):
                    case (1, 1):
                        t1 = 90
                        t2 = 270
                    case (2, 1):
                        t1 = 60
                        t2 = 300
                    case (3, 1):
                        t1 = 90
                        t2 = 360
                    case _:
                        print(f"Unsupported amount for circle: {(amount1, amount2)}")

                ax.add_patch(patches.Wedge(pos, style.legendRectsize2, t1, t2, lw=lw, fc=color1, ec=color1))
                ax.add_patch(patches.Wedge(pos, style.legendRectsize2, t2, t1, lw=lw, fc=color2, ec=color2))
            case _:
                print(f"Unsupported number of color values: {fc}")
    else:
        print(f"Unknown type for face color: {fc}")

def drawLegendCircle(ax, pos, text, style):
    x = pos[0] + style.legendRectsize2
    y = pos[1] + style.legendRectsize2
    drawCircle(ax, (x, y), style.legendShapeWidth, "none", "black", style)
    ax.text(pos[0] + style.legendSpace, pos[1] + style.legendRectsize2, text, size=style.legendFontSize, ha="left", va="center")

def drawDiamond(ax, pos, lw, fc, ec, style):
    x1 = pos[0] - style.legendRectsize2
    x2 = pos[0]
    x3 = pos[0] + style.legendRectsize2

    y1 = pos[1] - style.legendRectsize2
    y2 = pos[1]
    y3 = pos[1] + style.legendRectsize2

    if isinstance(fc, str):
        ax.add_patch(plt.Polygon([(x2, y1), (x1, y2), (x2, y3), (x3, y2)], lw=lw, fc=fc, ec=ec))
    elif isinstance(fc, list):
        match len(fc):
            case 1:
                color = "black"

                match fc[0]:
                    case Department.geo:
                        color = style.geoColor
                    case Department.bio:
                        color = style.bioColor
                    case Department.comp:
                        color = style.compColor
                    case _:
                        print(f"Unknown department: {fc}")

                ax.add_patch(plt.Polygon([(x2, y1), (x1, y2), (x2, y3), (x3, y2)], lw=lw, fc=color, ec=ec))

            case 2:
                (dp1, amount1) = fc[0]
                (dp2, amount2) = fc[1]
                color1 = departmentToColor(dp1, style)
                color2 = departmentToColor(dp2, style)

                match (amount1, amount2):
                    case (1, 1):
                        ax.add_patch(plt.Polygon([(x2, y1), (x2, y3), (x1, y2)], lw=lw, fc=color1, ec=color1))
                        ax.add_patch(plt.Polygon([(x2, y1), (x2, y3), (x3, y2)], lw=lw, fc=color2, ec=color2))
                    case (3, 1):
                        ax.add_patch(plt.Polygon([(x2, y2), (x2, y3), (x1, y2), (x2, y1), (x3, y2)], lw=lw, fc=color1, ec=color1))
                        ax.add_patch(plt.Polygon([(x2, y2), (x2, y3), (x3, y2)], lw=lw, fc=color2, ec=color2))
                    case _:
                        print(f"Unsupported amount for diamond: {(amount1, amount2)}")

            case _:
                print(f"Unsupported number of color values: {fc}")
    else:
        print(f"Unknown type for face color: {fc}")

def drawLegendDiamond(ax, pos, text, style):
    x = pos[0] + style.legendRectsize2
    y = pos[1] + style.legendRectsize2
    drawDiamond(ax, (x, y), style.legendShapeWidth, "none", "black", style)
    ax.text(pos[0] + style.legendSpace, pos[1] + style.legendRectsize2, text, size=style.legendFontSize, ha="left", va="center")

def drawTriangle(ax, pos, lw, fc, ec, style):
    sq3 = math.sqrt(3.0)
    x1 = pos[0] - style.legendRectsize2
    x2 = pos[0]
    x3 = pos[0] + style.legendRectsize2

    y1 = pos[1] - (style.legendRectsize / (2.0 * sq3))
    y2 = pos[1]
    y3 = pos[1] + (style.legendRectsize / sq3)

    if isinstance(fc, str):
        ax.add_patch(plt.Polygon([(x1, y1), (x2, y3), (x3, y1)], lw=lw, fc=fc, ec=ec))
    elif isinstance(fc, list):
        match len(fc):
            case 1:
                color = "black"

                match fc[0]:
                    case Department.geo:
                        color = style.geoColor
                    case Department.bio:
                        color = style.bioColor
                    case Department.comp:
                        color = style.compColor
                    case _:
                        print(f"Unknown department: {fc}")

                ax.add_patch(plt.Polygon([(x1, y1), (x2, y3), (x3, y1)], lw=lw, fc=color, ec=ec))

            case 2:
                (dp1, amount1) = fc[0]
                (dp2, amount2) = fc[1]
                color1 = departmentToColor(dp1, style)
                color2 = departmentToColor(dp2, style)

                match (amount1, amount2):
                    case (1, 1):
                        ax.add_patch(plt.Polygon([(x1, y1), (x2, y3), (x2, y1)], lw=lw, fc=color1, ec=color1))
                        ax.add_patch(plt.Polygon([(x2, y1), (x2, y3), (x3, y1)], lw=lw, fc=color2, ec=color2))
                    case (2, 1):
                        ax.add_patch(plt.Polygon([(x1, y1), (x3, y1), (x2, y2), (x2, y3)], lw=lw, fc=color1, ec=color1))
                        ax.add_patch(plt.Polygon([(x2, y2), (x3, y1), (x2, y3)], lw=lw, fc=color2, ec=color2))
                    case _:
                        print(f"Unsupported amount for triangle: {(amount1, amount2)}")
            case _:
                print(f"Unsupported number of color values: {fc}")
    else:
        print(f"Unknown type for face color: {fc}")

def drawLegendTriangle(ax, pos, text, style):
    x = pos[0] + style.legendRectsize2
    y = pos[1] + style.legendRectsize2
    drawTriangle(ax, (x, y), style.legendShapeWidth, "none", "black", style)
    ax.text(pos[0] + style.legendSpace, pos[1] + style.legendRectsize2, text, size=style.legendFontSize, ha="left", va="center")

def drawApp2020(ax, pos, c, style):
    ax.text(pos[0], pos[1] - 0.01, "§", size=style.legendSymbolSize, ha="center", va="center", c=c)

def drawApp2022(ax, pos, c, style):
    ax.text(pos[0], pos[1] - 0.06, "*", size=style.legendSymbolSize, ha="center", va="center", c=c)

def drawApp2023(ax, pos, c, style):
    ax.text(pos[0], pos[1] - 0.01, "+", size=style.legendSymbolSize, ha="center", va="center", c=c)

def drawApp2024(ax, pos, c, style):
    ax.text(pos[0], pos[1] - 0.01, "⊗", size=style.legendSymbolSize, ha="center", va="center", c=c)

def drawLegendApp2020(ax, pos, text, style):
    drawApp2020(ax, (pos[0] + style.legendRectsize2, pos[1] + style.legendRectsize2), "black", style)
    ax.text(pos[0] + style.legendSpace, pos[1] + style.legendRectsize2, text, size=style.legendFontSize, ha="left", va="center")

def drawLegendApp2022(ax, pos, text, style):
    drawApp2022(ax, (pos[0] + style.legendRectsize2, pos[1] + style.legendRectsize2), "black", style)
    ax.text(pos[0] + style.legendSpace, pos[1] + style.legendRectsize2, text, size=style.legendFontSize, ha="left", va="center")

def drawLegendApp2023(ax, pos, text, style):
    drawApp2023(ax, (pos[0] + style.legendRectsize2, pos[1] + style.legendRectsize2), "black", style)
    ax.text(pos[0] + style.legendSpace, pos[1] + style.legendRectsize2, text, size=style.legendFontSize, ha="left", va="center")

def drawLegendApp2024(ax, pos, text, style):
    drawApp2024(ax, (pos[0] + style.legendRectsize2, pos[1] + style.legendRectsize2), "black", style)
    ax.text(pos[0] + style.legendSpace, pos[1] + style.legendRectsize2, text, size=style.legendFontSize, ha="left", va="center")

def calcDist(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]

    return math.hypot(dx, dy)

def drawConnection(ax, pos1, pos2, count, style):
    lw = 2.0 + (count / 3.0)

    d = calcDist(pos1, pos2)

    if d <= style.thresholdDist:
        line = plt.Line2D([pos1[0], pos2[0]], [pos1[1], pos2[1]], lw=lw, c=style.connectionColor, zorder=1.0)
        ax.add_line(line)
    else:
        cpx = (pos1[0] + pos2[0]) / 2.0
        cpy = (pos1[1] + pos2[1]) / 2.0
        dx = (cpx - style.dataCenter[0]) / 2.0
        dy = (cpy - style.dataCenter[1]) / 2.0
        controllPoint = (cpx - dx, cpy - dy)
        vertices = [pos1, controllPoint, pos2]
        codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3]
        path = Path(vertices, codes)
        connection = patches.PathPatch(path, fc='none', ec=style.connectionColor, lw=lw)
        ax.add_patch(connection)

def drawLegend(ax, style):
    geoPos = style.legendPos
    drawLegendRect(ax, geoPos, style.geoColor, "Geosciences", style)

    bioPos = (geoPos[0], geoPos[1] - style.legendSpace)
    drawLegendRect(ax, bioPos, style.bioColor, "Biosciences", style)

    compPos = (bioPos[0], bioPos[1] - style.legendSpace)
    drawLegendRect(ax, compPos, style.compColor, "Computer Sciences", style)

    tuebingenPos = (compPos[0], compPos[1] - style.legendSpace)
    drawLegendCircle(ax, tuebingenPos, "University of Tübingen", style)

    hohenheimPos = (tuebingenPos[0], tuebingenPos[1] - style.legendSpace)
    drawLegendDiamond(ax, hohenheimPos, "University of Hohenheim", style)

    senkenbergPos = (hohenheimPos[0], hohenheimPos[1] - style.legendSpace)
    drawLegendTriangle(ax, senkenbergPos, "Senckenberg", style)

    #appointment2020Pos = (senkenbergPos[0], senkenbergPos[1] - style.legendSpace)
    #drawLegendApp2020(ax, appointment2020Pos, "appointment since 2020", style)

    appointment2022Pos = (senkenbergPos[0], senkenbergPos[1] - style.legendSpace)
    drawLegendApp2022(ax, appointment2022Pos, "appointment since 2022", style)

    #appointment2023Pos = (appointment2022Pos[0], appointment2022Pos[1] - style.legendSpace)
    #drawLegendApp2023(ax, appointment2023Pos, "appointment since 2023", style)

    appointment2024Pos = (appointment2022Pos[0], appointment2022Pos[1] - style.legendSpace)
    drawLegendApp2024(ax, appointment2024Pos, "appointed 2024", style)

def drawData(ax, style, data):
    (centerX, centerY) = style.dataCenter

    #ax.add_patch(plt.Circle((centerX, centerY), style.symbolRadius))

    number = float(len(data))

    print(f"Number of workgroups: {number}")

    angle = 90.0
    angleStep = 360.0 / number

    # Pre-calculate all positions:
    for wg in data:
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))

        wg.symbolPos = (centerX + (x * style.symbolRadius), centerY + (y * style.symbolRadius))
        wg.textPos = (centerX + (x * style.textRadius), centerY + (y * style.textRadius))

        if (angle == 90.0) or (angle == -90.0):
            wg.textAlignment = "center"
        elif (angle < 90.0) and (angle > -90.0):
            wg.textAlignment = "left"
        else:
            wg.textAlignment = "right"

        angle = angle - angleStep

    style.thresholdDist = calcDist(data[0].symbolPos, data[1].symbolPos) * 1.1

    # Draw connections:
    for wg1 in data:
        for (name2, count) in wg1.cooperations:
            for wg2 in data:
                if wg2.name == name2:
                    drawConnection(ax, wg1.symbolPos, wg2.symbolPos, count, style)
                    break

    # Draw Symbols:
    for wg in data:
        #(x, y)  = wg.pos
        if wg.institution == Institution.tuebingen:
            drawCircle(ax, wg.symbolPos, 0.3, wg.department, "none", style)
        elif wg.institution == Institution.hohenheim:
            drawDiamond(ax, wg.symbolPos, 0.3, wg.department, "none", style)
        elif wg.institution == Institution.senckenberg:
            drawTriangle(ax, wg.symbolPos, 0.3, wg.department, "none", style)
        else:
            print("Unknown institution: {wg.institution}")

        match wg.appointmentSince:
            case "2020":
                drawApp2020(ax, wg.symbolPos, "white", style)
            case "2022":
                drawApp2022(ax, wg.symbolPos, "white", style)
            case "2023":
                drawApp2023(ax, wg.symbolPos, "white", style)
            case "2024":
                drawApp2024(ax, wg.symbolPos, "white", style)
            case _:
                pass

    # Draw Text:
    for wg in data:
        ax.text(wg.textPos[0], wg.textPos[1], wg.name, ha=wg.textAlignment, size=style.legendFontSize)


def draw():
    print("Draw diagram")

    style = diagram_style.DiagramStyle()
    workgroups = cooperation_data.generateWorkgroups()

    # Init diagram:
    fig, ax = plt.subplots(figsize=(15.0, 10.0))
    ax.axis('equal')
    ax.axis('off')

    # Draw legend:
    drawLegend(ax, style)

    # Draw data:
    drawData(ax, style, workgroups)

    #ax.relim()
    ax.autoscale_view()

    plt.savefig("terra_cooperation_circle.svg")
    plt.savefig("terra_cooperation_circle.png")
    plt.show()

