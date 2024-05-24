class DiagramStyle:
    def __init__(self):
        print("Create default style")

        # Legend on the left
        self.geoColor = "#946c46"
        self.bioColor = "#316d1e"
        self.compColor = "#a11e3b"
        self.legendFont = ""
        self.legendFontSize = 15
        self.legendSymbolSize = 25
        self.legendPos = (0.0, 10.0)
        self.legendRectsize = 0.3
        self.legendRectsize2 = self.legendRectsize / 2.0
        self.legendRectsize3 = self.legendRectsize / 5.0
        self.legendSpace = self.legendRectsize + self.legendRectsize2
        self.legendShapeWidth = 3.0
        self.diagramCenter = (10.0, 5.0)
        self.diagramRadius = 5.0
        self.connectionColor = "#9d9c9c"
        self.workgroupCircleRadius = 1.0
        self.workgroupTriangleLength = 1.0
        self.workgroupDiamondLength = 1.0

        # Circle with data and connections
        self.dataCenter = (6.5, 9.0)
        self.symbolRadius = 2.0
        self.textRadius = self.symbolRadius + 0.3
        self.thresholdDist = 0.0

