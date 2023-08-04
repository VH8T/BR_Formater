"""
Copyright 2023 vh8t

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import subprocess
import sys

try:
    import wx
    import wx.adv
    import yaml
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "wxPython", "pyyaml"])
    import wx
    import wx.adv
    import yaml

cred = """
Credits:

This YAML brew recipe formatter tool is proudly made by vh8t. Its purpose is to facilitate the creation of YAML format files for brew recipes used with the Minecraft plugin named Brewery. You can find more information about Brewery on their official page.

Enjoy brewing and crafting your unique recipes with ease using this handy tool!"""
str_to_int = {"any": 0, "birch": 1, "oak": 2, "jungle": 3, "spruce": 4, "acacia": 5, "dark oak": 6, "crimson": 7,
              "warped": 8, "mangrove": 9}


class CreditsFrame(wx.Frame):
    def __init__(self, parent, title):
        super(CreditsFrame, self).__init__(parent, title=title, size=(400, 300),
                                           style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        credits_text = wx.StaticText(panel, label=cred)
        credits_text.Wrap(350)
        vbox.Add(credits_text, flag=wx.ALL, border=10)

        url_title = wx.StaticText(panel, label="Official Brewery page:")
        url_title.Wrap(350)
        vbox.Add(url_title, flag=wx.ALL, border=10)

        brewery_url = "https://dev.bukkit.org/projects/brewery"
        hyperlink = wx.adv.HyperlinkCtrl(panel, wx.ID_ANY, label=brewery_url)
        hyperlink.SetURL(brewery_url)
        vbox.Add(hyperlink, flag=wx.ALL, border=10)

        panel.SetSizer(vbox)
        self.Show()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(825, 430),
                                      style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        icon = wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        grid_sizer = wx.GridSizer(rows=15, cols=3, hgap=50, vgap=0)

        titles = ["Brew Name", "Ingredients", "Boiling Time", "Distill Runs", "Distill Time", "Wood Type", "Age",
                  "Color", "Difficulty", "Alcohol", "Lore", "Effects"]
        placeholders = ["Name of the brew", "Enter Ingredients", "Amount of minutes", "Amount of runs",
                        "Amount of seconds", "Type of wood", "Amount of years", "Color in HEX",
                        "Difficulty from 1 to 10", "Alcohol in %", "Lore text", "Effects text"]

        input_values = []

        for _ in range(6):
            if len(titles) == 12:
                for i in range(3):
                    title_label = wx.StaticText(panel, label="")
                    grid_sizer.Add(title_label, flag=wx.ALIGN_CENTER_HORIZONTAL)

            for title in titles[:3]:
                title_label = wx.StaticText(panel, label=title, size=(195, -1))
                grid_sizer.Add(title_label, flag=wx.ALIGN_CENTER_HORIZONTAL)
                titles.remove(title)

            for placeholder in placeholders[:3]:
                input_ctrl = wx.TextCtrl(panel, size=(200, -1))
                input_ctrl.SetHint(placeholder)
                grid_sizer.Add(input_ctrl, flag=wx.ALIGN_CENTER_HORIZONTAL)
                placeholders.remove(placeholder)
                input_values.append(input_ctrl)

            for i in range(3):
                title_label = wx.StaticText(panel, label="")
                grid_sizer.Add(title_label, flag=wx.ALIGN_CENTER_HORIZONTAL)

        vbox.Add(grid_sizer, flag=wx.ALIGN_CENTER)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        submit_button = wx.Button(panel, label="Submit")
        hbox.Add(submit_button, flag=wx.ALIGN_CENTER | wx.RIGHT, border=10)

        credits_button = wx.Button(panel, label="Credits")
        hbox.Add(credits_button, flag=wx.ALIGN_CENTER)

        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        submit_button.Bind(wx.EVT_BUTTON, self.on_submit)
        credits_button.Bind(wx.EVT_BUTTON, self.show_credits)

        panel.SetSizer(vbox)
        self.Show()

        submit_button.Bind(wx.EVT_BUTTON, self.on_submit)

        self.input_values = input_values

    def show_credits(self, event):
        credits_frame = CreditsFrame(self, title="Credits")
        credits_frame.Show()
        event.Skip()

    def on_submit(self, event):
        yaml_data = {}

        for title, input_ctrl in zip(
                ["Brew Name", "Ingredients", "Boiling Time", "Distill Runs", "Distill Time", "Wood Type", "Age",
                 "Color", "Difficulty", "Alcohol", "Lore", "Effects"], self.input_values):
            value = input_ctrl.GetValue().strip()
            if value:
                if title == "Brew Name":
                    title = title.lower().replace(" ", "_")
                elif title == "Ingredients":
                    value = [item.strip() for item in value.split(",")]
                    for i, v in enumerate(value):
                        parts = v.split(" ")
                        for j, part in enumerate(parts):
                            if part.isdigit():
                                parts[j - 1] = f"{parts[j - 1]}/{part}"
                                parts.pop(j)
                                break
                        value[i] = " ".join(parts)
                elif title in ["Lore", "Effects"]:
                    value = [item.strip() for item in value.split(",")]
                elif title in ["Boiling Time", "Distill Time", "Age", "Difficulty", "Alcohol", "Wood Type",
                               "Distill Runs"]:
                    if title == "Wood Type":
                        value = str_to_int[value.lower()]
                    else:
                        value = int(value)
                yaml_data[title.lower()] = value

        if yaml_data:
            brew_name = yaml_data.get("brew_name", "")
            if brew_name and brew_name != "":
                filename = f"{brew_name.lower().replace(' ', '_')}.yaml"

                formatted_yaml_data = {
                    "brew_name": {
                        "name": yaml_data.get("brew_name", ""),
                        "ingredients": yaml_data.get("ingredients", []),
                        "cookingtime": yaml_data.get("boiling time", 0),
                        "distillruns": yaml_data.get("distill runs", 0),
                        "distilltime": yaml_data.get("distill time", 0),
                        "wood": yaml_data.get("wood type", 0),
                        "age": yaml_data.get("age", 0),
                        "color": yaml_data.get("color", ""),
                        "difficulty": yaml_data.get("difficulty", 0),
                        "alcohol": yaml_data.get("alcohol", 0),
                        "lore": yaml_data.get("lore", []),
                        "effects": yaml_data.get("effects", [])
                    }
                }

                with open(filename, "w") as yaml_file:
                    yaml.dump(formatted_yaml_data, yaml_file, default_flow_style=False, sort_keys=False, indent=2)
            else:
                print("Brew name is required!")
        event.Skip()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "Brewery Recipe Formatter Tool")
    app.MainLoop()
