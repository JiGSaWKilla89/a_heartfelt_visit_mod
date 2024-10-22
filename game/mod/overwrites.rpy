init 6 python:
    def _remove_quest(self, id, category = ""):
        if category == "":
            category = self.is_in(id)
        try:
            del self.quests_dict[category][id]
            if self.quests_dict[category] == {}:
                del self.quests_dict[category]
        except KeyError as e:
            print(e)


init 1:# Character Overrides
    define subtitle = Character(None, color="#ffffff", what_font = "whatever.ttf", what_text_align=0.5, what_xalign=0.5, window_yalign=0.0, window_xfill=False, what_size = 50, what_outlines=[(3, "#000000")])
    define mc = Character("Me", color="#6495ED",  image="mc", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define joe = Character("Joe", color="#6495ED", image="joe", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define nina = Character("Nina", color="#DE3163", image="nina", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define nick = Character("Nicholas", color="#6495ED", image="nick", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define kate = Character("Kate", color="#DE3163", image="kate", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define lana = Character("Lana", color="#DE3163", image="lana", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define chloe = Character("Chloe", color="#DE3163", image="ch", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define jesse = Character("Jesse", color="#DE3163", image="jesse", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define monica = Character("Monica", color="#DE3163", image="monica", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define otis = Character("Otis", color="#6495ED", image="otis", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define kevin = Character("Kevin", color="#6495ED", image="kevin", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define markus = Character("Markus", color="#6495ED", image="markus", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define dani = Character("Dani", color="#DE3163", image="dani", what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define clerk = Character(None, what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define mec = Character(None, what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define nCenter = Character(None, what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.5, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define nCenterRed = Character(None, what_font = "Romanica.ttf", layout = "subtitle", what_color="#ff0000", what_text_align=0.5, what_xalign=0.5, window_yalign=0.5, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    define n = Character(None, what_font = "Romanica.ttf", layout = "subtitle", what_text_align=0.5, what_xalign=0.5, window_yalign=0.95, window_xfill=False, what_size = 50, what_outlines=[(5, "#1118", 0, 0), (3, "#111", 0, 0)])
    # The game starts here.

init python:
    text_corrections = {
        "Oh, MC…" : "Oh. [player_name]…"
        }

    def text_fixes(text):

        if text in text_corrections:
            return text_corrections[text]
        
        return text
    
    config.say_menu_text_filter = text_fixes