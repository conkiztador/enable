
from numpy import arange, array

from enthought.enable2.api import Canvas, Viewport, Window, Scrolled
from enthought.enable2.tools.api import ViewportPanTool
from enthought.enable2.primitives.api import Box
from enthought.enable2.example_support import demo_main, DemoFrame

class MyFrame(DemoFrame):

    def _create_window(self):

        canvas = Canvas(bgcolor="lightsteelblue", draw_axes=True)
        
        boxgridsize = 8
        boxsize = 50
        
        spacing = boxsize * 2
        offset = spacing / 2
        
        origin_color = array([0.0, 0.0, 1.0])
        x_color = array([0.0, 1.0, 0.0])
        y_color = array([1.0, 0.0, 0.0])
        
        for i in range(boxgridsize):
            for j in range(boxgridsize):
                color = tuple(x_color / (boxgridsize - 1) * i + \
                              y_color / (boxgridsize - 1) * j + \
                              origin_color) + (1.0,)
                box = Box(color=color, bounds=[boxsize, boxsize], resizable="")
                box.position= [i*spacing + offset - boxsize/2 + 0.5,
                               j*spacing + offset - boxsize/2 + 0.5]
                canvas.add(box)

        viewport = Viewport(component=canvas)
        viewport.view_position = [0,0]
        viewport.tools.append(ViewportPanTool(viewport))

        scrolled = Scrolled(canvas, fit_window = True,
                            inside_padding_width = 0,
                            mousewheel_scroll = False,
                            viewport_component = viewport,
                            always_show_sb = True,
                            continuous_drag_update = True)

        return Window(self, -1, component=scrolled)

if __name__ == "__main__":
    demo_main(MyFrame, title="Canvas example")