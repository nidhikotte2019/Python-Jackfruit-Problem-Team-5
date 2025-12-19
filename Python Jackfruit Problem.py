import random
import wx

movies = [{"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "vibe": "mind-bending"},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "vibe": "emotional"},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "vibe": "revolutionary"},
    {"title": "Blade Runner 2049", "genre": "Sci-Fi", "rating": 8.0, "vibe": "visual"},
    {"title": "Arrival", "genre": "Sci-Fi", "rating": 7.9, "vibe": "thoughtful"},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "vibe": "intense"},
    {"title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1, "vibe": "wild"},
    {"title": "Gladiator", "genre": "Action", "rating": 8.5, "vibe": "epic"},
    {"title": "John Wick", "genre": "Action", "rating": 7.9, "vibe": "stylish"},
    {"title": "Die Hard", "genre": "Action", "rating": 8.2, "vibe": "classic"},
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3, "vibe": "inspiring"},
    {"title": "Forrest Gump", "genre": "Drama", "rating": 8.8, "vibe": "heartwarming"},
    {"title": "The Pursuit of Happyness", "genre": "Drama", "rating": 8.0, "vibe": "motivating"},
    {"title": "12 Angry Men", "genre": "Drama", "rating": 9.0, "vibe": "powerful"},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8, "vibe": "thought-provoking"},
    {"title": "La La Land", "genre": "Romance", "rating": 8.0, "vibe": "dreamy"},
    {"title": "Pride and Prejudice", "genre": "Romance", "rating": 8.0, "vibe": "classic"},
    {"title": "The Notebook", "genre": "Romance", "rating": 7.9, "vibe": "emotional"},
    {"title": "Titanic", "genre": "Romance", "rating": 7.8, "vibe": "tragic"},
    {"title": "Before Sunrise", "genre": "Romance", "rating": 8.1, "vibe": "intimate"},
    {"title": "Parasite", "genre": "Thriller", "rating": 8.6, "vibe": "shocking"},
    {"title": "Se7en", "genre": "Thriller", "rating": 8.6, "vibe": "dark"},
    {"title": "Gone Girl", "genre": "Thriller", "rating": 8.1, "vibe": "twisty"},
    {"title": "The Silence of the Lambs", "genre": "Thriller", "rating": 8.6, "vibe": "chilling"},
    {"title": "Oldboy", "genre": "Thriller", "rating": 8.4, "vibe": "disturbing"},
    {"title": "Zootopia", "genre": "Animation", "rating": 8.0, "vibe": "fun"},
    {"title": "Spirited Away", "genre": "Animation", "rating": 8.6, "vibe": "magical"},
    {"title": "Coco", "genre": "Animation", "rating": 8.4, "vibe": "emotional"},
    {"title": "Toy Story", "genre": "Animation", "rating": 8.3, "vibe": "nostalgic"},
    {"title": "Finding Nemo", "genre": "Animation", "rating": 8.2, "vibe": "heartfelt"},
    {"title": "Conjuring", "genre": "Horror", "rating": 7.5, "vibe": "atmospheric tension"},
    {"title": "The Curse of La Llorona", "genre": "Horror", "rating": 5.3, "vibe": "eery"},
    {"title": "The Nun", "genre": "Horror", "rating": 5.4, "vibe": "frightening"},
    {"title": "The Ouija Board", "genre": "Horror", "rating": 4.5, "vibe": "scary"},
    {"title": "IT", "genre": "Horror", "rating": 7.3, "vibe": "spooky"},]

comments = ["This one will stay in your head long after the credits roll!",
    "Perfect if you want to feel all the feels 🎭",
    "A classic pick — you can't go wrong with this!",
    "Get your popcorn ready 🍿",
    "Trust me, this one hits different.",
    "Cinematic gold — you'll thank me later ✨",
    "Warning: you might rewatch this one immediately 🔁",
    "An underrated gem 💎",
    "Guaranteed to blow your mind 🤯",
    "Sit back, relax, and let this movie do its magic 🌟",
    "Movie night just got better 🎉",
    "If vibes were movies, this one is top-tier 🎬",
    "Keep tissues nearby for this one 😢",
    "High chance of goosebumps 🪶",
    "This one deserves a standing ovation 👏",
    "Not just a movie, an *experience* 🌌",
    "Legendary pick 🔥",
    "I call this a comfort movie — pure joy 😊",
    "Critics love it, but fans love it more ❤️",
    "This is the kind of movie you'll recommend to friends 📢"]

moods = {"sad": ["Drama", "Romance"],
    "happy": ["Comedy", "Animation"],
    "adventurous": ["Action", "Sci-Fi"],
    "thoughtful": ["Drama", "Sci-Fi"],
    "scary": ["Thriller", "Horror"],
    "romantic": ["Romance"]}

favourites = {}
watchlist = []
ratings = {}

def style_button(btn, bgc="#2563EB", fgc="#FFFFFF"):
    bg = wx.Colour(bgc)
    fg = wx.Colour(fgc)
    btn.SetBackgroundColour(bg)
    btn.SetForegroundColour(fg)

class MovieRecommenderFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="4K-Movie Recommender 🍿", size=(900, 650))
        self.last_movie = None
        self.InitUI()
    def InitUI(self):
        self.Centre()
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(15, 23, 42))
        font_title = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        font_label = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        font_normal = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        font_output = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        main = wx.BoxSizer(wx.VERTICAL)
        header = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(panel, label="🍿 4K-Movie Recommender")
        title.SetFont(font_title)
        title.SetForegroundColour(wx.Colour(248, 250, 252))
        subtitle = wx.StaticText(panel, label="Mood-based, smart and random picks for your movie night.")
        subtitle.SetFont(font_normal)
        subtitle.SetForegroundColour(wx.Colour(148, 163, 184))
        header.Add(title, flag=wx.ALL, border=5)
        header.Add(subtitle, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)
        main.Add(header, flag=wx.EXPAND | wx.ALL, border=10)
        input_box = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(panel, label="Enter a mood or genre (or pick from list):")
        label.SetFont(font_label)
        label.SetForegroundColour(wx.Colour(226, 232, 240))
        input_box.Add(label, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        row = wx.BoxSizer(wx.HORIZONTAL)
        self.input_text = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.input_text.SetFont(font_normal)
        self.input_text.SetHint("e.g. sad, happy, Sci-Fi, romantic...")
        self.input_text.Bind(wx.EVT_TEXT_ENTER, self.OnRecommend)
        row.Add(self.input_text, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        options = sorted(set(list(moods.keys()) + [m["genre"] for m in movies]))
        self.combo = wx.ComboBox(panel, choices=options, style=wx.CB_READONLY)
        self.combo.SetFont(font_normal)
        self.combo.Bind(wx.EVT_COMBOBOX, self.OnComboSelect)
        row.Add(self.combo, flag=wx.RIGHT, border=10)
        input_box.Add(row, flag=wx.EXPAND)
        info = wx.StaticText(panel, label="Moods: " + ", ".join(sorted(moods.keys())) + "\nGenres: " + ", ".join(sorted({m['genre'] for m in movies})))
        info.SetFont(font_normal)
        info.SetForegroundColour(wx.Colour(148, 163, 184))
        input_box.Add(info, flag=wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM, border=10)
        main.Add(input_box, flag=wx.EXPAND)
        btn_row1 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_recommend = wx.Button(panel, label="🎬 Recommend")
        self.btn_smart = wx.Button(panel, label="🤖 Smart")
        self.btn_random = wx.Button(panel, label="🎲 Random")
        self.btn_top = wx.Button(panel, label="🔥 Top 3")
        for b in [self.btn_recommend, self.btn_smart, self.btn_random, self.btn_top]:
            b.SetFont(font_normal)
        style_button(self.btn_recommend, "#22C55E")
        style_button(self.btn_smart, "#0EA5E9")
        style_button(self.btn_random, "#A855F7")
        style_button(self.btn_top, "#F97316")
        self.btn_recommend.Bind(wx.EVT_BUTTON, self.OnRecommend)
        self.btn_smart.Bind(wx.EVT_BUTTON, self.OnSmart)
        self.btn_random.Bind(wx.EVT_BUTTON, self.OnRandom)
        self.btn_top.Bind(wx.EVT_BUTTON, self.OnTop)
        for b in [self.btn_recommend, self.btn_smart, self.btn_random, self.btn_top]:
            btn_row1.Add(b, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        main.Add(btn_row1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        btn_row2 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_save = wx.Button(panel, label="💾 Save Last Movie")
        self.btn_rate = wx.Button(panel, label="⭐ Rate Last Movie")
        self.btn_watchlist = wx.Button(panel, label="📌 Show Watchlist")
        for b in [self.btn_save, self.btn_rate, self.btn_watchlist]:
            b.SetFont(font_normal)
            style_button(b, "#4F46E5")
        self.btn_watchlist.SetBackgroundColour(wx.Colour(100, 116, 139))
        self.btn_save.Bind(wx.EVT_BUTTON, self.OnSave)
        self.btn_rate.Bind(wx.EVT_BUTTON, self.OnRate)
        self.btn_watchlist.Bind(wx.EVT_BUTTON, self.OnShowWatchlist)
        for b in [self.btn_save, self.btn_rate, self.btn_watchlist]:
            btn_row2.Add(b, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        main.Add(btn_row2, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        self.output = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2 | wx.BORDER_NONE)
        self.output.SetFont(font_output)
        self.output.SetBackgroundColour(wx.Colour(15, 23, 42))
        self.output.SetForegroundColour(wx.Colour(248, 250, 252))
        self.output.SetValue("Welcome to the 4K-Movie Recommender 🎬\n"
            "───────────────────────────────────────\n"
            "• Type a mood or genre.\n"
            "• Try Smart for taste-based picks.\n"
            "• Use Save + Watchlist to track what to watch.\n\n")
        main.Add(self.output, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        panel.SetSizer(main)
        
    def print_movie(self, movie, header="🎬 Recommended Movie 🎬"):
        comment = random.choice(comments)
        text = (f"\n{header}\n"
            f"─────────────────────────────\n"
            f"Title : {movie['title']}\n"
            f"Genre : {movie['genre']}\n"
            f"Rating: {movie['rating']}/10\n"
            f"Vibe  : {movie['vibe']}\n"
            f"💡 {comment}\n")
        self.output.AppendText(text)
    def recommend_movie(self, choice):
        choice = choice.lower()
        if choice in moods:
            possible_genres = moods[choice]
            filtered = [m for m in movies if m["genre"] in possible_genres]
        else:
            filtered = [m for m in movies if choice in m["genre"].lower() or choice in m["vibe"].lower()]
        if not filtered:
            self.output.AppendText("\nI couldn't match that exactly, so here's a surprise pick! 🎉\n")
            movie = random.choice(movies)
        else:
            movie = random.choice(filtered)
            favourites[movie["genre"]] = favourites.get(movie["genre"], 0) + 1
        self.last_movie = movie
        self.print_movie(movie)
        return movie
    def smart_recommendation(self):
        if not favourites:
            self.output.AppendText("\nSmart mode needs a few choices first. Get some recommendations, then try again.\n")
            return None
        favorite_genre = max(favourites, key=favourites.get)
        filtered = [m for m in movies if m["genre"] == favorite_genre]
        movie = random.choice(filtered)
        self.last_movie = movie
        self.print_movie(movie, header="🤖 Smart Recommendation 🤖")
        return movie
    def random_pick(self):
        movie = random.choice(movies)
        if self.last_movie and len(movies) > 1:
            while movie == self.last_movie:
                movie = random.choice(movies)
        self.last_movie = movie
        self.print_movie(movie, header="🎲 Random Movie Pick 🎲")
        return movie
    def top_picks(self):
        picks = random.sample(movies, 3)
        text = "\n🔥 Today's Top Picks 🔥\n───────────────────────\n"
        for i, m in enumerate(picks, 1):
            text += f"{i}. {m['title']} ({m['genre']}, {m['rating']}/10) - {m['vibe']}\n"
        self.output.AppendText(text)
        
    def OnComboSelect(self, event):
        self.input_text.SetValue(self.combo.GetValue())
    def OnRecommend(self, event):
        choice = self.input_text.GetValue().strip()
        if choice:
            self.recommend_movie(choice)
            self.input_text.SetValue("")
    def OnSmart(self, event):
        self.smart_recommendation()
    def OnRandom(self, event):
        self.random_pick()
    def OnTop(self, event):
        self.top_picks()
    def OnSave(self, event):
        if not self.last_movie:
            wx.MessageBox("No movie to save yet. Get a recommendation first!", "Error", wx.ICON_WARNING)
            return
        title = self.last_movie["title"]
        if title not in watchlist:
            watchlist.append(title)
            wx.MessageBox(f"'{title}' added to watchlist. 📌", "Saved", wx.ICON_INFORMATION)
        else:
            wx.MessageBox(f"'{title}' is already in your watchlist.", "Info", wx.ICON_INFORMATION)
    def OnRate(self, event):
        if not self.last_movie:
            wx.MessageBox("No movie to rate yet. Get a recommendation first!", "Error", wx.ICON_WARNING)
            return
        dlg = wx.SingleChoiceDialog(self, f"Rate '{self.last_movie['title']}' (0–10):", "Rate Movie", [str(i) for i in range(11)])
        if dlg.ShowModal() == wx.ID_OK:
            score = int(dlg.GetStringSelection())
            ratings[self.last_movie["title"]] = score
            wx.MessageBox(f"Thanks! You rated '{self.last_movie['title']}' {score}/10 ⭐", "Rating saved", wx.ICON_INFORMATION)
        dlg.Destroy()
    def OnShowWatchlist(self, event):
        if not watchlist:
            wx.MessageBox("Your watchlist is empty. Save a movie first!", "Watchlist", wx.ICON_INFORMATION)
            return
        text = ""
        for i, title in enumerate(watchlist, 1):
            text += f"{i}. {title} - Your rating: {ratings.get(title, 'Not rated')}\n"
        dlg = wx.MessageDialog(self, text, "Your Watchlist", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
def main():
    app = wx.App()
    frame = MovieRecommenderFrame()
    frame.Show()
    app.MainLoop()
if __name__ == "__main__":
    main()
