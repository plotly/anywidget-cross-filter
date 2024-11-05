import marimo

__generated_with = "0.9.14"
app = marimo.App()


@app.cell
def __():
    import plotly.express as px
    import plotly.graph_objects as go
    from random import randint
    import marimo as mo
    return go, mo, px, randint


@app.cell
def __(randint):
    y1 = [randint(0, 10) for i in range(0, 10)]
    return (y1,)


@app.cell
def __(go, mo, px, y1):
    fig1 = px.scatter(x=range(0, 10), y=y1)
    fig1.update_layout(dragmode="select")

    widget1 = go.FigureWidget(fig1)

    trace1 = widget1.data[0]

    mo.ui.anywidget(widget1)
    return fig1, trace1, widget1


@app.cell
def __(go, mo, px, y1):
    fig2 = px.scatter(x=range(0, 10), y=y1)
    fig2.update_layout(dragmode="select")

    widget2 = go.FigureWidget(fig2)

    trace2 = widget2.data[0]

    mo.ui.anywidget(widget2)
    return fig2, trace2, widget2


@app.cell
def __(trace1, trace2, widget1, widget2):
    def update_to_red(trace, points, selector):
        c = ["#636efa"] * len(trace.x)

        for i in points.point_inds:
            c[i] = "red"
            with widget2.batch_update():
                trace2.marker.color = c


    trace1.on_selection(update_to_red)


    def update_to_orange(trace, points, selector):
        c = ["#636efa"] * len(trace.x)

        for i in points.point_inds:
            c[i] = "orange"
            with widget1.batch_update():
                trace1.marker.color = c


    trace2.on_selection(update_to_orange)
    return update_to_orange, update_to_red


if __name__ == "__main__":
    app.run()
