from shiny import App, render, ui
from load_bruv_training import BRUVDataFramesFromExcelFile
from main import main


app_ui = ui.page_fluid(
    ui.h2("BRUV Checker"),
    ui.a("Link to source code", href="https://github.com/koleh-tech/bruv_checker"),
    ui.input_file("file", "File"),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        if not input.file():
            return "Please upload a file"
        filename = input.file()[0]["datapath"]
        bruv_data_frames = BRUVDataFramesFromExcelFile(filename)
        return main(bruv_data_frames)

app = App(app_ui, server)
