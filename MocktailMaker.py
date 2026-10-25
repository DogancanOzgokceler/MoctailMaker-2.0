# Doğancan Özgökçeler — Mocktail Maker 2.0 (Final + TR/EN)

#𒁲𒈠𒃶𒈨𒂗
#Ⲛⲟϥⲣⲓ

import tkinter as tk
from tkinter import ttk, font
import random

# ─── Renkler ───────────────────────────────────────────────────────────────────
BG_DARK   = "#0e0e1c"
BG_CARD   = "#16162a"
BG_PANEL  = "#1c1c36"
BORDER    = "#2e2e52"
TEXT_MAIN = "#f0f0ff"
TEXT_DIM  = "#7777aa"

FLAVOR_COLORS = {
    "caffeine":    "#4d96ff",
    "fruit":       "#ff9e7a",
    "spice":       "#ff6b6b",
    "refreshment": "#6bcb77",
    "sweet":       "#ffd93d",
    "sour":        "#c3f73a",
}

# ══════════════════════════════════════════════════════════════════════════════
# ÇEVIRI / TRANSLATIONS
# ══════════════════════════════════════════════════════════════════════════════
TRANSLATIONS = {
    "TR": {
        "title":        "✨  Mocktail Maker 2.0  ✨",
        "subtitle":     "Lezzet tercihlerini puanla — sana özel kokteylini yaratalım",
        "flavor_title": "LEZZET PUANLARIN",
        "style_title":  "İÇECEK STİLİ",
        "result_title": "KOKTEYLİN",
        "ingredients":  "MALZEMELER",
        "match_score":  "EŞLEŞME SKORU",
        "other_recs":   "DİĞER ÖNERİLER",
        "craft_btn":    "⚗️   KOKTEYLİMİ HAZIRLA",
        "reset_btn":    "↺  Sıfırla",
        "placeholder":  "Puanlarını gir ve\nKOKTEYLİMİ HAZIRLA'ya bas!",
        "waiting":      "kokteylini bekliyor",
        "match_pct":    "%{} eşleşme",
        "warn_empty":   "⚠️  En az bir lezzeti puanla!",
        "flavors": [
            ("caffeine",    "☕  Kafein",   "0=Kafeinsiz · 5=Çok güçlü"),
            ("fruit",       "🍓  Meyve",    "0=Meyvesiz · 5=Çok meyveli"),
            ("spice",       "🌶️  Baharat",  "0=Baharatsız · 5=Çok baharatlı"),
            ("refreshment", "🌿  Ferahlık", "0=Ağır · 5=Çok ferahlatıcı"),
            ("sweet",       "🍯  Tatlılık", "0=Tatsız · 5=Çok tatlı"),
            ("sour",        "🍋  Ekşilik",  "0=Ekşisiz · 5=Çok ekşi"),
        ],
        "style_checks": [
            ("🫧  Köpüklü / Gazlı",  "#4d96ff"),
            ("☕  Sıcak / Kışlık",    "#c0392b"),
            ("🌿  Hafif & Ferah",     "#6bcb77"),
            ("💥  Yoğun & Güçlü",    "#ff6b6b"),
        ],
        "ing_labels": ["Baz", "Meyve", "Baharat", "Ferahlık", "Ekstra"],
        "desc_templates": [
            "{bev}  •  {fr}  •  {sp} ile özenle hazırlandı.",
            "Taze {fr} bazlı, {ref} ile tamamlandı.",
            "{bev} üzerine kişisel dokunuşlarla yaratıldı.",
        ],
    },
    "EN": {
        "title":        "✨  Mocktail Maker 2.0  ✨",
        "subtitle":     "Rate your flavor preferences — let us craft your perfect drink",
        "flavor_title": "YOUR FLAVOR RATINGS",
        "style_title":  "DRINK STYLE",
        "result_title": "YOUR COCKTAIL",
        "ingredients":  "INGREDIENTS",
        "match_score":  "MATCH SCORE",
        "other_recs":   "OTHER SUGGESTIONS",
        "craft_btn":    "⚗️   CRAFT MY COCKTAIL",
        "reset_btn":    "↺  Reset",
        "placeholder":  "Rate your flavors and\nhit CRAFT MY COCKTAIL!",
        "waiting":      "waiting for your cocktail",
        "match_pct":    "{}% match",
        "warn_empty":   "⚠️  Please rate at least one flavor!",
        "flavors": [
            ("caffeine",    "☕  Caffeine",    "0=No caffeine · 5=Very strong"),
            ("fruit",       "🍓  Fruit",       "0=No fruit · 5=Very fruity"),
            ("spice",       "🌶️  Spice",       "0=No spice · 5=Very spicy"),
            ("refreshment", "🌿  Refreshment", "0=Heavy · 5=Very refreshing"),
            ("sweet",       "🍯  Sweetness",   "0=Not sweet · 5=Very sweet"),
            ("sour",        "🍋  Sourness",    "0=Not sour · 5=Very sour"),
        ],
        "style_checks": [
            ("🫧  Sparkling / Fizzy",  "#4d96ff"),
            ("☕  Warm / Cozy",         "#c0392b"),
            ("🌿  Light & Fresh",       "#6bcb77"),
            ("💥  Bold & Intense",      "#ff6b6b"),
        ],
        "ing_labels": ["Base", "Fruit", "Spice", "Refreshment", "Extra"],
        "desc_templates": [
            "Carefully crafted with {bev}  •  {fr}  •  {sp}.",
            "Fresh {fr}-based, finished with {ref}.",
            "Built on {bev} with personal touches.",
        ],
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# MALZEME HAVUZLARI — (isim_TR, isim_EN, ağırlık)
# ══════════════════════════════════════════════════════════════════════════════

BEVERAGES = {
    0: [
        ("Maden Suyu",          "Mineral Water",        10),
        ("Soda Water",          "Soda Water",            8),
        ("Sparkling Water",     "Sparkling Water",       8),
        ("Sprite",              "Sprite",                7),
        ("Gazoz",               "Lemon Soda",            7),
        ("Tonic Water",         "Tonic Water",           6),
        ("Hindistan Cevizi Suyu","Coconut Water",        5),
        ("Elma Suyu",           "Apple Juice",           5),
        ("Beyaz Üzüm Suyu",     "White Grape Juice",     3),
    ],
    1: [
        ("Sprite",              "Sprite",               10),
        ("Gazoz",               "Lemon Soda",            9),
        ("Ginger Ale",          "Ginger Ale",            8),
        ("Maden Suyu",          "Mineral Water",         6),
        ("Limonata",            "Lemonade",              8),
        ("Taze Sıkılmış Limonata","Fresh Lemonade",      5),
        ("Tonik",               "Tonic",                 5),
        ("Elma Suyu",           "Apple Juice",           4),
    ],
    2: [
        ("Ginger Ale",          "Ginger Ale",           10),
        ("Fanta",               "Fanta",                 9),
        ("Fanta Limon",         "Fanta Lemon",           5),
        ("Limonata",            "Lemonade",              8),
        ("Portakallı Gazoz",    "Orange Soda",           6),
        ("Sprite",              "Sprite",                5),
        ("Vişneli Soda",        "Cherry Soda",           4),
    ],
    3: [
        ("Fanta",               "Fanta",                10),
        ("Cola",                "Cola",                  8),
        ("Cola Zero",           "Cola Zero",             5),
        ("Light Cola",          "Diet Cola",             4),
        ("Portakallı Gazoz",    "Orange Soda",           7),
        ("Çay (Soğuk)",         "Iced Tea",              6),
        ("Yeşil Çay (Soğuk)",   "Iced Green Tea",        5),
    ],
    4: [
        ("Cola",                "Cola",                 10),
        ("Light Cola",          "Diet Cola",             7),
        ("Cola Zero",           "Cola Zero",             6),
        ("Soğuk Brew Kahve",    "Cold Brew Coffee",      8),
        ("Ice Tea",             "Iced Tea",              8),
        ("Çay (Soğuk)",         "Iced Tea",              5),
        ("Yeşil Çay (Soğuk)",   "Iced Green Tea",        4),
    ],
    5: [
        ("Soğuk Brew Kahve",    "Cold Brew Coffee",     10),
        ("Espresso (Soğuk)",    "Iced Espresso",         8),
        ("Ice Tea",              "Iced Tea",              7),
        ("Cola",                "Cola",                  6),
        ("Cola Zero",           "Cola Zero",             4),
        ("Çay Özü (Konsantre)",  "Concentrated Tea",      3),
    ],
}

FRUITS = {
    0: None,
    1: [
        ("Limon Suyu",          "Lemon Juice",          10),
        ("Misket Limonu Suyu",  "Lime Juice",            8),
        ("Greyfurt Suyu",       "Grapefruit Juice",      6),
        ("Mandalina Suyu",      "Tangerine Juice",       5),
    ],
    2: [
        ("Portakal Suyu",       "Orange Juice",         10),
        ("Mandalina Suyu",      "Tangerine Juice",       8),
        ("Greyfurt Suyu",       "Grapefruit Juice",      7),
        ("Limon Suyu",          "Lemon Juice",           6),
        ("Altın Elma Suyu",     "Golden Apple Juice",    5),
    ],
    3: [
        ("Portakal Suyu",       "Orange Juice",         10),
        ("Ananas Suyu",         "Pineapple Juice",       9),
        ("Yeşil Elma Suyu",     "Green Apple Juice",     8),
        ("Nar Suyu",            "Pomegranate Juice",     7),
        ("Mandalina Suyu",      "Tangerine Juice",       6),
        ("Şeftali Suyu",        "Peach Juice",           5),
        ("Kayısı Suyu",         "Apricot Juice",         4),
    ],
    4: [
        ("Mango Suyu",          "Mango Juice",          10),
        ("Şeftali Suyu",        "Peach Juice",           9),
        ("Çilek Püresi",        "Strawberry Puree",      8),
        ("Karpuz Suyu",         "Watermelon Juice",      8),
        ("Ahududu Püresi",      "Raspberry Puree",       7),
        ("Ananas Suyu",         "Pineapple Juice",       6),
        ("Vişne Suyu",          "Sour Cherry Juice",     5),
        ("Böğürtlen Püresi",    "Blackberry Puree",      4),
    ],
    5: [
        ("Mango Suyu",          "Mango Juice",          10),
        ("Karpuz Suyu",         "Watermelon Juice",      9),
        ("Çilek Püresi",        "Strawberry Puree",      9),
        ("Ahududu Püresi",      "Raspberry Puree",       8),
        ("Böğürtlen Püresi",    "Blackberry Puree",      7),
        ("Marakuya Suyu",       "Passion Fruit Juice",   7),
        ("Yaban Mersini Suyu",  "Blueberry Juice",       6),
        ("Kavun Suyu",          "Melon Juice",           5),
        ("Şeftali Nektarı",     "Peach Nectar",          5),
    ],
}

SPICES = {
    0: None,
    1: [
        ("Vanilya Şurubu",      "Vanilla Syrup",        12),
        ("Gül Şurubu",          "Rose Syrup",            8),
        ("Karamel Şurubu",      "Caramel Syrup",         7),
        ("Hibiskus Şurubu",     "Hibiscus Syrup",        6),
        ("Lavanta Şurubu",      "Lavender Syrup",        5),
        ("Fesleğen Şurubu",     "Basil Syrup",           4),
    ],
    2: [
        ("Vanilya Şurubu",      "Vanilla Syrup",        10),
        ("Tarçın Şurubu",       "Cinnamon Syrup",        9),
        ("Hibiskus Şurubu",     "Hibiscus Syrup",        8),
        ("Karanfil Şurubu",     "Clove Syrup",           6),
        ("Lavanta Şurubu",      "Lavender Syrup",        6),
        ("Gül Suyu",            "Rose Water",            5),
        ("Zencefil Şurubu",      "Ginger Syrup",          5),
        ("Kakule Şurubu",        "Cardamom Syrup",        4),
    ],
    3: [
        ("Tarçın Şurubu",        "Cinnamon Syrup",       10),
        ("Zencefil Şurubu",      "Ginger Syrup",          9),
        ("Kakule Şurubu",        "Cardamom Syrup",        8),
        ("Karanfil Şurubu",      "Clove Syrup",           7),
        ("Hibiskus Şurubu",      "Hibiscus Syrup",        7),
        ("Anason Şurubu",        "Anise Syrup",           5),
        ("Yıldız Anason",        "Star Anise",            4),
        ("Zerdeçal Şurubu",      "Turmeric Syrup",        4),
    ],
    4: [
        ("Zencefil Şurubu",      "Ginger Syrup",         10),
        ("Kakule Şurubu",        "Cardamom Syrup",        8),
        ("Karanfil Şurubu",      "Clove Syrup",           8),
        ("Tarçın Şurubu (Güçlü)","Cinnamon Syrup (Strong)",7),
        ("Anason Şurubu",        "Anise Syrup",           6),
        ("Zerdeçal+Zencefil Şurubu","Turmeric+Ginger Syrup",6),
        ("Muskat Şurubu",         "Nutmeg Syrup",          4),
        ("Karabiber Şurubu",     "Black Pepper Syrup",    3),
    ],
    5: [
        ("Zencefil Şurubu (Yoğun)","Ginger Syrup (Strong)",10),
        ("Karanfil Şurubu",       "Clove Syrup",           9),
        ("Karanfil Şurubu",      "Clove Syrup",           8),
        ("Jalapeño Şurubu",      "Jalapeño Syrup",        6),
        ("Karabiber Şurubu",     "Black Pepper Syrup",    5),
        ("Zerdeçal+Karabiber Şurubu","Turmeric+Pepper Syrup",4),
    ],
}

REFRESHMENTS = {
    0: None,
    1: [
        ("Limon Dilimi",         "Lemon Slice",          12),
        ("Portakal Dilimi",      "Orange Slice",         10),
        ("Misket Limonu Dilimi", "Lime Slice",            8),
        ("Sitrus Kabuğu",        "Citrus Zest",           6),
        ("Mandalina Dilimi",     "Tangerine Slice",       4),
    ],
    2: [
        ("Limon Dilimleri",      "Lemon Slices",         12),
        ("Portakal Dilimleri",   "Orange Slices",        10),
        ("Misket Limonu",        "Lime Wedge",            9),
        ("Taze Nane Yaprağı",    "Fresh Mint Leaf",       8),
        ("Mandalina Dilimi",     "Tangerine Slice",       6),
        ("Greyfurt Dilimi",      "Grapefruit Slice",      4),
    ],
    3: [
        ("Taze Nane",            "Fresh Mint",           12),
        ("Limon Dilimleri",      "Lemon Slices",         10),
        ("Misket Limonu",        "Lime Wedge",            9),
        ("Portakal Dilimleri",   "Orange Slices",         8),
        ("Salatalık Dilimleri",  "Cucumber Slices",       5),
        ("Greyfurt Dilimi",      "Grapefruit Slice",      5),
        ("Fesleğen Yaprakları",  "Basil Leaves",          3),
    ],
    4: [
        ("Taze Nane (Bol)",      "Fresh Mint (Heavy)",   12),
        ("Limon + Nane",         "Lemon + Mint",         10),
        ("Misket Limonu + Nane", "Lime + Mint",           9),
        ("Kırık Buz",            "Crushed Ice",           7),
        ("Salatalık Suyu",       "Cucumber Juice",        6),
        ("Greyfurt Suyu",        "Grapefruit Juice",      5),
        ("Portakal Kabuğu",      "Orange Peel",           3),
    ],
    5: [
        ("Taze Nane (Bol)",      "Fresh Mint (Heavy)",   12),
        ("Limon + Nane",         "Lemon + Mint",         11),
        ("Misket Limonu + Nane", "Lime + Mint",          10),
        ("Kırık Buz (Bol)",      "Crushed Ice (Heavy)",   7),
        ("Salatalık Suyu",       "Cucumber Juice",        6),
        ("Greyfurt Dilimleri",   "Grapefruit Slices",     5),
        ("Mentol Damlası",       "Menthol Drops",         3),
    ],
}

EXTRAS_SWEET = [
    ("Bal",                    "Honey",                10),
    ("Krem Şanti",             "Whipped Cream",         9),
    ("Karamel Şurubu",         "Caramel Syrup",         8),
    ("Şeker Kenarı",           "Sugar Rim",             7),
    ("Agave Şurubu",           "Agave Syrup",           6),
    ("Hurma Şurubu",           "Date Syrup",            5),
    ("Çilek Garnisi",          "Strawberry Garnish",    4),
    ("Portakal Dilimi",        "Orange Slice",          3),
]
EXTRAS_SOUR = [
    ("Tuz Kenarı",             "Salt Rim",             10),
    ("Limon Dilimi",           "Lemon Slice",           9),
    ("Misket Limonu",          "Lime Wedge",            8),
    ("Greyfurt Dilimi",        "Grapefruit Slice",      6),
    ("Nar Taneleri",           "Pomegranate Seeds",     5),
    ("Nar Taneleri",           "Pomegranate Seeds",     4),
]
EXTRAS_NEUTRAL = [
    ("Buz Küpleri",            "Ice Cubes",            10),
    ("Kırık Buz",              "Crushed Ice",           9),
    ("Limon Dilimi",           "Lemon Slice",           7),
    ("Taze Nane Yaprağı",      "Fresh Mint Leaf",       7),
    ("Portakal Kabuğu",        "Orange Peel",           5),
    ("Kurutulmuş Çiçekler",    "Dried Flowers",         4),
    ("Çilek Garnisi",          "Strawberry Garnish",    3),
]

COCKTAIL_NAMES = {
    "dark_spicy":  [
        ("Cola Sunrise",        "#c0392b", "🍒"),
        ("Fire & Cola",         "#e74c3c", "🌶️"),
        ("Midnight Kick",       "#2c3e50", "🍇"),
        ("Dark Espresso Storm", "#6f4e37", "☕"),
        ("Spiced Cola",         "#8e44ad", "🍓"),
        ("Ember Cola",          "#8b0000", "🌶️"),
        ("Dark Spice Rush",     "#c0392b", "🍒"),
        ("Doğancan's Special",  "#0d7377", "🌿"),
    ],
    "dark_fruity": [
        ("Café Tropical",       "#d35400", "🥭"),
        ("Cola Berry Burst",    "#c0392b", "🍒"),
        ("Dark Mango Rush",     "#e67e22", "🥭"),
        ("Midnight Berry",      "#8e44ad", "🍇"),
        ("Coffee Peach Dream",  "#6f4e37", "🍑"),
        ("Cherry Cola",         "#c0392b", "🍒"),
        ("Dark Passion",        "#6f2da8", "🫐"),
        ("Velvet Berry",        "#7b2d8b", "🍇"),
        ("Blue Fox Lady's Kiss","#1565c0", "🫐"),
    ],
    "light_spicy": [
        ("Ginger Blossom",      "#27ae60", "🌸"),
        ("Clove & Citrus",      "#8b4513", "🍋"),
        ("Turmeric Sunrise",    "#f0a500", "🌺"),
        ("Anise Garden",        "#2ecc71", "🌿"),
        ("Hibiscus Pepper",     "#c0392b", "🌺"),
        ("Cinnamon Apple",      "#d35400", "🍎"),
        ("Spiced Blossom",      "#c77dff", "🌸"),
        ("Fire Garden",         "#ff6b6b", "🌿"),
        ("Doğancan's Special",  "#0d7377", "🌿"),
    ],
    "light_fruity": [
        ("Watermelon Breeze",   "#e74c3c", "🍉"),
        ("Mango Coconut Dream", "#f39c12", "🥭"),
        ("Strawberry Bloom",    "#ff6b6b", "🍓"),
        ("Peach Blossom",       "#e8a87c", "🍑"),
        ("Berry Garden",        "#9b59b6", "🫐"),
        ("Tropical Sunset",     "#1abc9c", "🌺"),
        ("Kiwi Breeze",         "#2ecc71", "🥝"),
        ("Cherry Blossom",      "#c0392b", "🌸"),
        ("Passion Fruit Dream", "#f39c12", "🍊"),
        ("Raspberry Bloom",     "#e91e8c", "🍓"),
        ("Melon Splash",        "#52c97a", "🍈"),
        ("Apricot Garden",      "#e67e22", "🍑"),
        ("Blue Fox Lady's Kiss","#1565c0", "🫐"),
    ],
    "light_floral": [
        ("Rose Lemonade",       "#e91e8c", "🌹"),
        ("Lavender Spritz",     "#a29bfe", "🌸"),
        ("Hibiscus Garden",     "#c0392b", "🌺"),
        ("Elderflower Dream",   "#ffeaa7", "🌼"),
        ("Violet Mist",         "#8e44ad", "🌷"),
        ("Cherry Blossom Fizz", "#ffb7c5", "🌸"),
        ("Jasmine Breeze",      "#f5f5dc", "🌼"),
        ("Blue Fox Lady's Kiss","#1565c0", "🫐"),
        ("Iris Garden",         "#7b68ee", "🌷"),
        ("Magnolia Dream",      "#ffcba4", "🌸"),
    ],
    "refreshing": [
        ("Cucumber Mint",       "#52c97a", "🥒"),
        ("Garden Ginger Mule",  "#27ae60", "🌿"),
        ("Lemon Garden",        "#a8e063", "🍋"),
        ("Coconut Ice",         "#4d96ff", "🥥"),
        ("Arctic Mint",         "#00b4d8", "❄️"),
        ("Snow Cooler",         "#aee8f8", "🌨️"),
        ("Frozen Garden",       "#b8f0a0", "🍃"),
        ("Ice Blossom",         "#52c97a", "🌸"),
        ("Doğancan's Special",  "#0d7377", "🌿"),
        ("Mint Glacier",        "#00c9d4", "❄️"),
        ("Fresh Lime Splash",   "#6bcb77", "🍋"),
    ],
    "sweet_creamy": [
        ("Peach Vanilla Dream", "#e8a87c", "🍑"),
        ("Caramel Honey Cloud", "#d4a017", "🍯"),
        ("Vanilla Sunset",      "#f5cba7", "🌸"),
        ("Honey Cream Soda",    "#f7dc6f", "🍯"),
        ("Strawberry Cream",    "#ffb7c5", "🍓"),
        ("Mango Honey Fizz",    "#f39c12", "🥭"),
        ("Peach Melba Dream",   "#ffb347", "🍑"),
        ("Coconut Blossom",     "#ffefd5", "🥥"),
    ],
    "citrus_sour": [
        ("Grapefruit Twist",    "#ff6b6b", "🍋"),
        ("Lemon Burst",         "#f1c40f", "🍋"),
        ("Citrus Garden",       "#e67e22", "🍊"),
        ("Sour Berry Pop",      "#9b59b6", "🫐"),
        ("Pomegranate Sour",    "#c0392b", "🌺"),
        ("Lime & Chili",        "#2ecc71", "🌶️"),
        ("Tangy Blossom",       "#ff9e7a", "🍊"),
        ("Sharp Citrus",        "#ffd93d", "🍋"),
        ("Doğancan's Special",  "#0d7377", "🌿"),
    ],
    "default": [
        ("Garden Blend",        "#9b59b6", "🌿"),
        ("Fruit Harmony",       "#3498db", "🍓"),
        ("Blossom Mix",         "#1abc9c", "🌸"),
        ("Secret Garden",       "#27ae60", "🌺"),
        ("Seasonal Special",    "#8e44ad", "🍊"),
        ("Blue Fox Lady's Kiss","#1565c0", "🫐"),
        ("Doğancan's Special",  "#0d7377", "🌿"),
        ("Crystal Garden",      "#00b4d8", "❄️"),
    ],
}

# ══════════════════════════════════════════════════════════════════════════════
# GÜNÜN İÇECEK BİLGİLERİ
# ══════════════════════════════════════════════════════════════════════════════
DAILY_DRINK_FACTS = [
    ("🍋 Limonata", "Limonata, tarihte bilinen en eski içeceklerden biridir. Mısır'da M.S. 1000 yılında limon suyu, şeker ve su karıştırılarak yapıldığı kayıtlara geçmiştir.", "Lemonade is one of the oldest known beverages. Records from Egypt around 1000 AD describe mixing lemon juice, sugar and water together."),
    ("🌿 Nane Çayı", "Nane, sindirim sistemi için doğal bir çözümdür. İçerdiği mentol sayesinde mide kramplarını ve bulantıyı giderir, aynı zamanda zihni ferahlatır.", "Mint is a natural remedy for the digestive system. Its menthol content relieves stomach cramps and nausea, while also refreshing the mind."),
    ("🥥 Hindistan Cevizi Suyu", "Hindistan cevizi suyu, doğanın en iyi elektrolit kaynağıdır. Potasyum açısından bir muzdan daha zengindir ve vücudu hızla nemlendirir.", "Coconut water is nature's best electrolyte source. It contains more potassium than a banana and rapidly hydrates the body."),
    ("🍹 Mocktail Nedir?", "Mocktail kelimesi 'mock' (sahte) ve 'cocktail' kelimelerinin birleşiminden gelir. Alkolsüz ama görsel ve lezzet açısından zengin içeceklerdir.", "The word 'mocktail' combines 'mock' and 'cocktail'. These are non-alcoholic drinks that are visually stunning and full of flavor."),
    ("🌺 Hibiskus", "Hibiskus çiçeğinden yapılan içecekler, C vitamini bakımından portakala rakip olacak kadar zengindir. Kırmızı-mor rengi doğal antosiyaninlerden gelir.", "Hibiscus drinks rival oranges in vitamin C content. Their red-purple color comes from natural anthocyanins."),
    ("🫐 Yaban Mersini", "Yaban mersini, dünyada en yüksek antioksidan içeriğine sahip meyveler arasında yer alır. Beyin sağlığını desteklediği bilimsel çalışmalarla kanıtlanmıştır.", "Blueberries rank among the world's highest antioxidant fruits. Scientific studies have proven their benefits for brain health."),
    ("🍊 Portakal", "Bir bardak taze portakal suyu, günlük C vitamini ihtiyacının tamamını karşılar. Portakal suyu içmek, bağışıklık sistemini güçlendirir.", "A glass of fresh orange juice meets your entire daily vitamin C requirement. Drinking orange juice strengthens the immune system."),
    ("🌸 Gül Suyu", "Gül suyu, yüzyıllardır hem mutfakta hem de güzellikte kullanılmaktadır. Osmanlı sarayının vazgeçilmez içeceğiydi; şerbetlere eklenirdi.", "Rose water has been used in both cooking and beauty for centuries. It was an indispensable drink in the Ottoman palace, added to sherbets."),
    ("🥭 Mango", "Mango, 'meyvelerin kralı' olarak bilinir. Hindistan'da 4.000 yılı aşkın bir süredir yetiştirilmekte olup dünyanın en çok tüketilen tropikal meyvesidir.", "Mango is known as the 'king of fruits'. It has been cultivated in India for over 4,000 years and is the world's most consumed tropical fruit."),
    ("❄️ Buz", "Buz, içecekleri soğutmaktan çok daha fazlasını yapar. Doğru boyutta buz kullanmak içeceğin tadını değiştirir — büyük buz yavaş erir ve içeceği daha az seyreltirir.", "Ice does much more than just cool drinks. Using the right size ice changes the taste — larger ice melts slowly and dilutes drinks less."),
    ("🍉 Karpuz", "Karpuzun %92'si sudur. Bu yüzden yaz aylarında en iyi doğal nemlendirici olarak kabul edilir. Aynı zamanda kalp sağlığını destekleyen likopen içerir.", "Watermelon is 92% water, making it the best natural hydrator in summer. It also contains lycopene that supports heart health."),
    ("🌶️ Zencefil", "Zencefil, 5.000 yılı aşkın bir süredir hem baharat hem de ilaç olarak kullanılmaktadır. Bulantı karşıtı etkisi, tüm doğal çözümler arasında en güçlü olanlardan biridir.", "Ginger has been used as both spice and medicine for over 5,000 years. Its anti-nausea effect is among the strongest of all natural remedies."),
    ("🍑 Şeftali", "Şeftali, Çin'den dünyaya yayılmıştır. M.Ö. 2000 yılında Çin'de yetiştirilmeye başlanan şeftali, İpek Yolu aracılığıyla Avrupa'ya ulaşmıştır.", "The peach spread to the world from China. First cultivated in China around 2000 BC, it reached Europe via the Silk Road."),
    ("🌿 Fesleğen", "Fesleğen, antik Mısır'da kutsal bir bitki olarak kabul edilirdi. Günümüzde de stres azaltıcı özellikleri ile dikkat çekicidir.", "Basil was considered a sacred plant in ancient Egypt. Today it stands out for its stress-reducing properties."),
    ("🍋 Misket Limonu", "Misket limonu, limondan daha yüksek asit içerir ve kokteyllerde keskin bir ferahlık sağlar. C vitamini oranı yüksektir ve bağışıklığı destekler.", "Lime has higher acidity than lemon and provides a sharp freshness in cocktails. High in vitamin C, it supports immunity."),
]

# ── Malzeme bilgileri + Wikipedia linkleri ─────────────────────────────────
INGREDIENT_FACTS = [
    ("🌿 Nane",          "Nane, sindirime yardımcı olur ve ağız tazeleyici etkisi ile bilinir. Dünya genelinde en yaygın kullanılan aromatik bitkilerden biridir.",                "Mint aids digestion and is known for its breath-freshening effect.",          "Mentha"),
    ("🍋 Limon",          "Limon, C vitamini deposudur. Antik çağlardan bu yana hem mutfakta hem de tıpta kullanılmıştır.",                                                         "Lemon is a treasure of vitamin C, used in both cooking and medicine since ancient times.", "Lemon"),
    ("🥥 Hindistan Cevizi","Hindistan cevizi, Güneydoğu Asya'nın simgesidir. Suyu, yağı ve eti farklı amaçlarla kullanılan çok yönlü bir meyvedir.",                              "Coconut is the symbol of Southeast Asia — its water, oil and flesh each serve different purposes.", "Coconut"),
    ("🌺 Hibiskus",       "Hibiskus çiçeği, antioksidan bakımından son derece zengindir ve kan basıncını düşürücü etkisiyle bilinir.",                                              "Hibiscus flower is extremely rich in antioxidants and known for its blood pressure-lowering effect.", "Hibiscus"),
    ("🌸 Lavanta",        "Lavanta, sakinleştirici etkisiyle bilinir. Fransız Provence bölgesinin simgesi olan lavanta, içeceklere eşsiz bir çiçek aroması katar.",                 "Lavender is known for its calming effect. The symbol of French Provence, it adds a unique floral aroma.", "Lavender"),
    ("🌿 Fesleğen",       "Fesleğen, İtalyan mutfağının vazgeçilmezidir. Anti-inflamatuar özellikleri ve taze kokusuyla içeceklere benzersiz bir tat katar.",                        "Basil is indispensable in Italian cuisine. Its anti-inflammatory properties add a unique taste.", "Basil"),
    ("🫚 Zencefil",       "Zencefil, hem sıcak hem soğuk içeceklerde kullanılan güçlü bir baharattır. Bağışıklık sistemi üzerindeki olumlu etkileri bilimsel olarak kanıtlanmıştır.", "Ginger is a powerful spice used in both hot and cold drinks. Its positive effects on immunity are scientifically proven.", "Ginger"),
    ("🌰 Kakule",         "Kakule, dünyanın en pahalı baharatları arasındadır. Hint ve Orta Doğu mutfaklarında yüzyıllardır kullanılan kakule, içeceklere egzotik bir aroma katar.", "Cardamom is among the world's most expensive spices, adding an exotic aroma.", "Cardamom"),
    ("🌿 Tarçın",         "Tarçın, antik Mısır'dan bu yana kullanılan köklü bir baharattır. Kan şekerini dengeleme etkisi modern bilimle de doğrulanmıştır.",                        "Cinnamon has been used since ancient Egypt. Its blood sugar balancing effect has been confirmed by modern science.", "Cinnamon"),
    ("🌸 Gül Suyu",       "Gül suyu, Orta Doğu ve Güney Asya mutfaklarının en sevilen aromasıdır. Ruh halini iyileştirici etkisi bitkisel tıpta uzun zamandır bilinmektedir.",      "Rose water is a beloved aroma in Middle Eastern and South Asian cuisines, known for its mood-lifting effect.", "Rose_water"),
    ("💛 Zerdeçal",       "Zerdeçal, güçlü anti-inflamatuar bileşeni kurkumin ile öne çıkar. Altın sarısı rengi ve toprak kokusu içeceklere özgün bir karakter katar.",              "Turmeric stands out with its powerful anti-inflammatory compound curcumin and earthy aroma.", "Turmeric"),
    ("🫐 Yaban Mersini",  "Yaban mersini, beyin fonksiyonlarını desteklediği kanıtlanmış nadir meyvelerden biridir. Antioksidan içeriği son derece yüksektir.",                       "Blueberry is one of the rare fruits proven to support brain function, with extremely high antioxidant content.", "Blueberry"),
    ("🍑 Şeftali",        "Şeftali, A ve C vitaminleri ile lif bakımından zengindir. Tatlı ve yumuşak yapısıyla içeceklere kremsi bir doku katar.",                                   "Peach is rich in vitamins A and C and fiber, adding a creamy texture to drinks.", "Peach"),
    ("🥭 Mango",          "Mango, tropik meyvelerin en besleyicilerinden biridir. 20'den fazla vitamin ve mineral içeren mango, 'süper meyve' olarak anılmaktadır.",                  "Mango is one of the most nutritious tropical fruits, called a 'superfruit' for containing over 20 vitamins and minerals.", "Mango"),
    ("🍉 Karpuz",         "Karpuz, yüksek su içeriğiyle doğanın elektrolit içeceğidir. Kasları destekleyen amino asit sitrülin bakımından da oldukça zengindir.",                     "Watermelon is nature's electrolyte drink with its high water content, also rich in citrulline amino acid.", "Watermelon"),
    ("🌿 Anason",         "Anason, binlerce yıldır tüm dünyada kullanılan kadim bir baharattır. Sindirime yardımcı olur ve içeceklere tatlı-meyan kökü benzeri bir tat katar.",       "Anise is an ancient spice used worldwide for thousands of years, aiding digestion and adding a sweet licorice-like flavor.", "Anise"),
]

def weighted_choice(pool):
    items   = [item[0] for item in pool]
    weights = [item[-1] for item in pool]
    return random.choices(items, weights=weights, k=1)[0]

def weighted_choice_bilingual(pool, lang):
    idx = 0 if lang == "TR" else 1
    items   = [item[idx] for item in pool]
    weights = [item[-1]  for item in pool]
    return random.choices(items, weights=weights, k=1)[0]

def get_ingredient(pool_dict, score, lang, skip_zero_prob=0.82):
    if score == 0 and random.random() < skip_zero_prob:
        return None
    score = max(0, min(5, score))
    pool = pool_dict.get(score)
    if not pool:
        return None
    return weighted_choice_bilingual(pool, lang)


# ─── Bubble ────────────────────────────────────────────────────────────────────
class Bubble:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.reset(start=True)

    def reset(self, start=False):
        self.x = random.uniform(20, self.w - 20)
        self.y = random.uniform(0, self.h) if start else self.h + 10
        self.r = random.uniform(2, 7)
        self.speed = random.uniform(0.3, 1.0)
        self.drift = random.uniform(-0.25, 0.25)
        self.color = random.choice(list(FLAVOR_COLORS.values()))

    def step(self):
        self.y -= self.speed
        self.x += self.drift
        if self.y < -10:
            self.reset()


# ─── Uygulama ──────────────────────────────────────────────────────────────────
class CocktailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mocktail Maker 2.0  —  by Doğancan")
        self.root.geometry("1100x800")
        self.root.minsize(900, 650)
        self.root.configure(bg=BG_DARK)
        self.root.resizable(True, True)
        self._last_name = ""
        self.lang = "TR"  # Varsayılan dil

        self._fonts()
        self._styles()
        self._build()
        self._start_animations()

    def T(self, key):
        """Aktif dile göre çeviri döndür."""
        return TRANSLATIONS[self.lang][key]

    def _fonts(self):
        self.f_title = font.Font(family="Georgia",   size=24, weight="bold")
        self.f_sub   = font.Font(family="Georgia",   size=10, slant="italic")
        self.f_label = font.Font(family="Helvetica", size=9,  weight="bold")
        self.f_body  = font.Font(family="Helvetica", size=10)
        self.f_name  = font.Font(family="Georgia",   size=15, weight="bold")
        self.f_small = font.Font(family="Helvetica", size=8)
        self.f_tick  = font.Font(family="Helvetica", size=7)

    def _styles(self):
        s = ttk.Style()
        s.theme_use("clam")
        s.configure("Horizontal.TScale",
                    background=BG_PANEL, troughcolor=BG_DARK,
                    sliderthickness=14, sliderrelief="flat", borderwidth=0)

    # ── Layout ─────────────────────────────────────────────────────────────────
    def _build(self):
        # Header
        self.hdr = tk.Canvas(self.root, height=110, bg=BG_DARK, highlightthickness=0)
        self.hdr.pack(fill=tk.X)
        self._draw_header_bg()
        self.title_id = self.hdr.create_text(
            550, 44, text=self.T("title"),
            font=self.f_title, fill=TEXT_MAIN, anchor="center")
        self.subtitle_id = self.hdr.create_text(
            550, 82, text=self.T("subtitle"),
            font=self.f_sub, fill=TEXT_DIM, anchor="center")

        # Dil butonu — sağ üst köşe
        self.lang_btn = tk.Button(
            self.hdr, text="🌍 EN", font=self.f_small,
            bg="#2a2a50", fg=TEXT_MAIN, activebackground="#3a3a70",
            activeforeground=TEXT_MAIN, relief=tk.FLAT, bd=0,
            padx=10, pady=5, cursor="hand2",
            command=self._toggle_lang)
        self.lang_btn.place(relx=1.0, rely=0.0, x=-14, y=12, anchor="ne")

        # Baloncuk şeridi
        self.bub_canvas = tk.Canvas(self.root, height=40, bg=BG_DARK, highlightthickness=0)
        self.bub_canvas.pack(fill=tk.X)
        self.bubbles = [Bubble(1100, 40) for _ in range(28)]

        # Gövde
        body = tk.Frame(self.root, bg=BG_DARK)
        body.pack(fill=tk.BOTH, expand=True, padx=16, pady=(4, 16))
        body.columnconfigure(0, weight=4, minsize=340)
        body.columnconfigure(1, weight=6, minsize=460)
        body.rowconfigure(0, weight=1)

        lo = tk.Frame(body, bg=BG_PANEL)
        lo.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        lo.rowconfigure(0, weight=1)
        lo.columnconfigure(0, weight=1)
        self._build_left_scrollable(lo)

        right = tk.Frame(body, bg=BG_CARD)
        right.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        right.rowconfigure(0, weight=1)
        right.columnconfigure(0, weight=1)
        self._build_right(right)

    def _draw_header_bg(self):
        for y in range(110):
            frac = y / 110
            r = int(14 + frac * 8); g = int(14 + frac * 4); b = int(28 + frac * 26)
            self.hdr.create_line(0, y, 3000, y, fill=f"#{r:02x}{g:02x}{b:02x}")

    # ── Dil değiştirme ─────────────────────────────────────────────────────────
    def _toggle_lang(self):
        self.lang = "EN" if self.lang == "TR" else "TR"
        btn_text = "🌍 TR" if self.lang == "EN" else "🌍 EN"
        self.lang_btn.config(text=btn_text)
        self._refresh_ui()

    def _refresh_ui(self):
        """Dil değişince tüm statik metinleri güncelle."""
        self.hdr.itemconfig(self.title_id,    text=self.T("title"))
        self.hdr.itemconfig(self.subtitle_id, text=self.T("subtitle"))
        self.lbl_flavor_title.config(text=self.T("flavor_title"))
        self.lbl_style_title.config(text=self.T("style_title"))
        self.lbl_result_title.config(text=self.T("result_title"))
        self.lbl_ing_title.config(text=self.T("ingredients"))
        self.lbl_score_title.config(text=self.T("match_score"))
        self.lbl_other_title.config(text=self.T("other_recs"))
        self.craft_btn.config(text=self.T("craft_btn"))
        self.reset_btn.config(text=self.T("reset_btn"))
        # Slider etiketleri
        for (key, label, hint), lbl_widget, hint_widget in zip(
                self.T("flavors"), self.flavor_lbl_widgets, self.flavor_hint_widgets):
            lbl_widget.config(text=label)
            hint_widget.config(text=hint)
        # Stil checkbox'ları
        for (text, col), cb in zip(self.T("style_checks"), self.style_checkboxes):
            cb.config(text=text, fg=col)
        # Sonuç placeholder
        self.lbl_name.config(text=self.T("placeholder"))
        self.lbl_desc.config(text="")

    # ── Sol Panel ──────────────────────────────────────────────────────────────
    def _build_left_scrollable(self, outer):
        canvas = tk.Canvas(outer, bg=BG_PANEL, highlightthickness=0, bd=0)
        sb = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=sb.set)
        canvas.grid(row=0, column=0, sticky="nsew")
        sb.grid(row=0, column=1, sticky="ns")
        outer.columnconfigure(0, weight=1)
        inner = tk.Frame(canvas, bg=BG_PANEL)
        iid = canvas.create_window((0, 0), window=inner, anchor="nw")
        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(iid, width=e.width))
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        self._build_left_content(inner)

    def _build_left_content(self, p):
        self.lbl_flavor_title = tk.Label(p, text=self.T("flavor_title"),
                 font=self.f_label, bg=BG_PANEL, fg="#ffd93d", pady=10)
        self.lbl_flavor_title.pack(fill=tk.X, padx=16)
        tk.Frame(p, height=1, bg=BORDER).pack(fill=tk.X, padx=16, pady=(0, 6))

        self.vars = {}
        self.val_labels = {}
        self.flavor_lbl_widgets  = []
        self.flavor_hint_widgets = []

        for key, label, hint in self.T("flavors"):
            color = FLAVOR_COLORS[key]
            row = tk.Frame(p, bg=BG_PANEL)
            row.pack(fill=tk.X, padx=14, pady=(4, 0))
            top = tk.Frame(row, bg=BG_PANEL)
            top.pack(fill=tk.X)
            lbl_w = tk.Label(top, text=label, font=self.f_label,
                             bg=BG_PANEL, fg=color, anchor="w")
            lbl_w.pack(side=tk.LEFT)
            self.flavor_lbl_widgets.append(lbl_w)
            vl = tk.Label(top, text="0", font=self.f_label,
                          bg=BG_PANEL, fg=TEXT_MAIN, width=2, anchor="e")
            vl.pack(side=tk.RIGHT, padx=(0, 4))
            self.val_labels[key] = vl
            var = tk.IntVar(value=0)
            self.vars[key] = var
            ttk.Scale(row, from_=0, to=5, variable=var,
                      orient=tk.HORIZONTAL).pack(fill=tk.X, pady=(2, 0))
            ticks = tk.Frame(row, bg=BG_PANEL)
            ticks.pack(fill=tk.X)
            for t in ["0","1","2","3","4","5"]:
                tk.Label(ticks, text=t, font=self.f_tick,
                         bg=BG_PANEL, fg=TEXT_DIM).pack(side=tk.LEFT, expand=True)
            hint_w = tk.Label(row, text=hint, font=self.f_tick,
                              bg=BG_PANEL, fg=TEXT_DIM, anchor="w")
            hint_w.pack(fill=tk.X, pady=(1, 4))
            self.flavor_hint_widgets.append(hint_w)

            def _cb(k=key, vl=vl):
                def cb(*_): vl.config(text=str(self.vars[k].get()))
                return cb
            var.trace_add("write", _cb())

        tk.Frame(p, height=1, bg=BORDER).pack(fill=tk.X, padx=16, pady=(14, 6))
        self.lbl_style_title = tk.Label(p, text=self.T("style_title"),
                 font=self.f_label, bg=BG_PANEL, fg="#4d96ff")
        self.lbl_style_title.pack(anchor="w", padx=16)

        self.chk_sparkling = tk.BooleanVar()
        self.chk_warm      = tk.BooleanVar()
        self.chk_light     = tk.BooleanVar()
        self.chk_bold      = tk.BooleanVar()
        self.style_checkboxes = []

        for (text, col), var in zip(self.T("style_checks"),
                [self.chk_sparkling, self.chk_warm, self.chk_light, self.chk_bold]):
            cb = tk.Checkbutton(p, text=text, variable=var, font=self.f_body,
                                bg=BG_PANEL, fg=col, activebackground=BG_PANEL,
                                activeforeground=TEXT_MAIN, selectcolor=BG_DARK,
                                anchor="w", cursor="hand2")
            cb.pack(fill=tk.X, padx=16, pady=2)
            self.style_checkboxes.append(cb)

        tk.Frame(p, height=1, bg=BORDER).pack(fill=tk.X, padx=16, pady=(14, 8))

        self.craft_btn = tk.Button(
            p, text=self.T("craft_btn"),
            font=self.f_label, bg="#ff6b6b", fg=TEXT_MAIN,
            activebackground="#cc4444", activeforeground=TEXT_MAIN,
            relief=tk.FLAT, bd=0, padx=10, pady=12,
            cursor="hand2", command=self._generate)
        self.craft_btn.pack(fill=tk.X, padx=16)
        self._hover(self.craft_btn, "#ff6b6b", "#cc4444")

        self.reset_btn = tk.Button(
            p, text=self.T("reset_btn"), font=self.f_small,
            bg=BG_DARK, fg=TEXT_DIM, activebackground=BORDER,
            activeforeground=TEXT_MAIN, relief=tk.FLAT, bd=0,
            padx=6, pady=7, cursor="hand2", command=self._reset)
        self.reset_btn.pack(fill=tk.X, padx=16, pady=(6, 20))

    # ── Sağ Panel ──────────────────────────────────────────────────────────────
    def _build_right(self, p):
        top = tk.Frame(p, bg=BG_CARD)
        top.pack(fill=tk.X, padx=20, pady=(10, 0))
        self.lbl_result_title = tk.Label(top, text=self.T("result_title"),
                 font=self.f_label, bg=BG_CARD, fg="#ffd93d")
        self.lbl_result_title.pack(side=tk.LEFT)
        tk.Frame(p, height=1, bg=BORDER).pack(fill=tk.X, padx=20, pady=(4, 0))

        # ── Üst: bardak + tarif detayları ──────────────────────────────────
        content = tk.Frame(p, bg=BG_CARD)
        content.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
        content.columnconfigure(0, weight=0)
        content.columnconfigure(1, weight=1)
        content.rowconfigure(0, weight=1)

        lc = tk.Frame(content, bg=BG_CARD, width=170)
        lc.grid(row=0, column=0, sticky="ns", padx=(0, 14))
        lc.pack_propagate(False)
        self.glass = tk.Canvas(lc, width=150, height=300,
                               bg=BG_CARD, highlightthickness=0)
        self.glass.pack(pady=(16, 0))
        self._draw_empty_glass()

        rc = tk.Frame(content, bg=BG_CARD)
        rc.grid(row=0, column=1, sticky="nsew")
        rc.rowconfigure(0, weight=1)
        rc.columnconfigure(0, weight=1)

        dc = tk.Canvas(rc, bg=BG_CARD, highlightthickness=0, bd=0)
        dc.grid(row=0, column=0, sticky="nsew")
        di = tk.Frame(dc, bg=BG_CARD)
        did = dc.create_window((0, 0), window=di, anchor="nw")
        di.bind("<Configure>", lambda e: dc.configure(scrollregion=dc.bbox("all")))
        dc.bind("<Configure>", lambda e: dc.itemconfig(did, width=e.width))

        self.lbl_name = tk.Label(di, text=self.T("placeholder"),
                                 font=self.f_name, bg=BG_CARD, fg=TEXT_DIM,
                                 wraplength=280, justify="left")
        self.lbl_name.pack(anchor="w", pady=(14, 4))
        self.lbl_desc = tk.Label(di, text="", font=self.f_body, bg=BG_CARD,
                                 fg=TEXT_DIM, wraplength=280, justify="left")
        self.lbl_desc.pack(anchor="w", pady=(0, 10))

        tk.Frame(di, height=1, bg=BORDER).pack(fill=tk.X, pady=6)
        self.lbl_ing_title = tk.Label(di, text=self.T("ingredients"),
                 font=self.f_label, bg=BG_CARD, fg="#6bcb77")
        self.lbl_ing_title.pack(anchor="w", pady=(2, 4))
        self.ing_frame = tk.Frame(di, bg=BG_CARD)
        self.ing_frame.pack(fill=tk.X, pady=(0, 8))

        tk.Frame(di, height=1, bg=BORDER).pack(fill=tk.X, pady=6)
        self.lbl_score_title = tk.Label(di, text=self.T("match_score"),
                 font=self.f_label, bg=BG_CARD, fg="#4d96ff")
        self.lbl_score_title.pack(anchor="w", pady=(2, 4))
        self.score_bar = tk.Canvas(di, height=22, bg=BG_CARD, highlightthickness=0)
        self.score_bar.pack(fill=tk.X, pady=(0, 8))

        # ── Skor + Tek öneri yan yana ──────────────────────────────────────
        tk.Frame(di, height=1, bg=BORDER).pack(fill=tk.X, pady=6)

        score_row = tk.Frame(di, bg=BG_CARD)
        score_row.pack(fill=tk.X, pady=(0, 12))
        score_row.columnconfigure(0, weight=3)
        score_row.columnconfigure(1, weight=2)

        # Sol: skor başlık + bar
        score_left = tk.Frame(score_row, bg=BG_CARD)
        score_left.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        self.lbl_other_title = tk.Label(score_left,
                 text=self.T("other_recs"),
                 font=self.f_label, bg=BG_CARD, fg=TEXT_DIM)
        self.lbl_other_title.pack(anchor="w", pady=(2, 4))
        self.runner_frame = tk.Frame(score_left, bg=BG_CARD)
        self.runner_frame.pack(fill=tk.X)

        # Sağ: tek öneri kutusu
        self.suggest_box = tk.Frame(score_row, bg="#1a1a35",
                                    relief=tk.FLAT)
        self.suggest_box.grid(row=0, column=1, sticky="nsew")
        tk.Label(self.suggest_box,
                 text="💡 " + ("Belki de..." if self.lang=="TR" else "Maybe..."),
                 font=self.f_small, bg="#1a1a35", fg=TEXT_DIM,
                 anchor="w", padx=6).pack(fill=tk.X, pady=(4,2))
        self.suggest_name_lbl = tk.Label(self.suggest_box,
                 text="—", font=font.Font(family="Georgia", size=9, weight="bold"),
                 bg="#1a1a35", fg=TEXT_DIM,
                 wraplength=130, justify="left",
                 anchor="w", padx=6)
        self.suggest_name_lbl.pack(fill=tk.X, pady=(0, 6))

        # ══════════════════════════════════════════════════════════════════════
        # ALT KISIM: Günün bilgisi + Malzeme bilgisi + Geliştirici
        # ══════════════════════════════════════════════════════════════════════
        tk.Frame(p, height=2, bg=BORDER).pack(fill=tk.X, padx=12, pady=(0, 8))

        bottom = tk.Frame(p, bg=BG_DARK)
        bottom.pack(fill=tk.X, padx=12, pady=(0, 12))
        bottom.columnconfigure(0, weight=3)
        bottom.columnconfigure(1, weight=2)
        bottom.rowconfigure(0, weight=1)

        # ── Sol: Günün içecek bilgisi (büyük kutu) ─────────────────────────
        daily_fact = random.choice(DAILY_DRINK_FACTS)
        daily_title  = daily_fact[0]
        daily_text   = daily_fact[1] if self.lang == "TR" else daily_fact[2]

        self.daily_box = tk.Frame(bottom, bg="#12122a", relief=tk.FLAT)
        self.daily_box.grid(row=0, column=0, sticky="nsew", padx=(0, 6))

        # Başlık şeridi
        daily_header = tk.Frame(self.daily_box, bg="#1e1e40")
        daily_header.pack(fill=tk.X)
        tk.Label(daily_header,
                 text="☀️  GÜNÜN İÇECEK BİLGİSİ" if self.lang=="TR" else "☀️  DRINK FACT OF THE DAY",
                 font=self.f_label, bg="#1e1e40", fg="#ffd93d",
                 pady=6, padx=10, anchor="w").pack(fill=tk.X)

        self.daily_title_lbl = tk.Label(self.daily_box,
                 text=daily_title,
                 font=font.Font(family="Georgia", size=11, weight="bold"),
                 bg="#12122a", fg="#6bcb77",
                 anchor="w", padx=10)
        self.daily_title_lbl.pack(fill=tk.X, pady=(6,2))

        self.daily_text_lbl = tk.Label(self.daily_box,
                 text=daily_text,
                 font=self.f_body, bg="#12122a", fg=TEXT_MAIN,
                 wraplength=280, justify="left",
                 anchor="nw", padx=10)
        self.daily_text_lbl.pack(fill=tk.X, pady=(0,10))

        # ── Sağ: üst = malzeme bilgisi, alt = geliştirici ──────────────────
        right_col = tk.Frame(bottom, bg=BG_DARK)
        right_col.grid(row=0, column=1, sticky="nsew", padx=(6, 0))
        right_col.rowconfigure(0, weight=3)
        right_col.rowconfigure(1, weight=1)
        right_col.columnconfigure(0, weight=1)

        # Malzeme bilgisi kutusu (tıklanabilir → Wikipedia)
        ing_fact = random.choice(INGREDIENT_FACTS)
        self._current_wiki = ing_fact[3]

        self.ing_fact_box = tk.Frame(right_col, bg="#0e1a2e",
                                     relief=tk.FLAT, cursor="hand2")
        self.ing_fact_box.grid(row=0, column=0, sticky="nsew", pady=(0, 6))

        ing_header = tk.Frame(self.ing_fact_box, bg="#0a1628")
        ing_header.pack(fill=tk.X)
        tk.Label(ing_header,
                 text="🔬  MALZEME BİLGİSİ  🔗" if self.lang=="TR" else "🔬  INGREDIENT FACT  🔗",
                 font=self.f_label, bg="#0a1628", fg="#4d96ff",
                 pady=6, padx=8, anchor="w").pack(fill=tk.X)

        self.ing_fact_name = tk.Label(self.ing_fact_box,
                 text=ing_fact[0],
                 font=font.Font(family="Helvetica", size=10, weight="bold"),
                 bg="#0e1a2e", fg="#ff9e7a",
                 anchor="w", padx=8)
        self.ing_fact_name.pack(fill=tk.X, pady=(4,2))

        self.ing_fact_text = tk.Label(self.ing_fact_box,
                 text=ing_fact[1] if self.lang=="TR" else ing_fact[2],
                 font=self.f_small, bg="#0e1a2e", fg=TEXT_MAIN,
                 wraplength=200, justify="left",
                 anchor="nw", padx=8)
        self.ing_fact_text.pack(fill=tk.X, pady=(0,4))

        wiki_hint = tk.Label(self.ing_fact_box,
                 text="Wikipedia'da oku →" if self.lang=="TR" else "Read on Wikipedia →",
                 font=self.f_small, bg="#0e1a2e", fg="#4d96ff",
                 anchor="e", padx=8)
        wiki_hint.pack(fill=tk.X, pady=(0,6))

        # Tıklama olayları
        for w in [self.ing_fact_box, ing_header, self.ing_fact_name,
                  self.ing_fact_text, wiki_hint]:
            w.bind("<Button-1>", self._open_wiki)
            w.bind("<Enter>",    lambda e, f=self.ing_fact_box:
                   f.config(bg="#142038"))
            w.bind("<Leave>",    lambda e, f=self.ing_fact_box:
                   f.config(bg="#0e1a2e"))

        # Geliştirici kutusu (tıklanabilir → YouTube)
        self.dev_box = tk.Frame(right_col, bg="#1a0e2e",
                                relief=tk.FLAT, cursor="hand2")
        self.dev_box.grid(row=1, column=0, sticky="nsew")

        dev_header = tk.Frame(self.dev_box, bg="#120a22")
        dev_header.pack(fill=tk.X)
        tk.Label(dev_header,
                 text="👨‍💻  GELİŞTİRİCİYİ TANI  🎬" if self.lang=="TR" else "👨‍💻  MEET THE DEVELOPER  🎬",
                 font=self.f_label, bg="#120a22", fg="#c77dff",
                 pady=5, padx=8, anchor="w").pack(fill=tk.X)

        dev_text = (
            "Bu uygulamanın ilk geliştiricisi\nDoğancan Özgökçeler'i tanıyın  →"
            if self.lang == "TR" else
            "Meet the original developer\nDoğancan Özgökçeler  →"
        )
        self.dev_lbl = tk.Label(self.dev_box,
                 text=dev_text,
                 font=self.f_small, bg="#1a0e2e", fg=TEXT_MAIN,
                 wraplength=200, justify="left",
                 anchor="nw", padx=8, pady=6)
        self.dev_lbl.pack(fill=tk.X)

        for w in [self.dev_box, dev_header, self.dev_lbl]:
            w.bind("<Button-1>", self._open_youtube)
            w.bind("<Enter>",    lambda e, f=self.dev_box: f.config(bg="#241438"))
            w.bind("<Leave>",    lambda e, f=self.dev_box: f.config(bg="#1a0e2e"))

    # ── Bardak ─────────────────────────────────────────────────────────────────
    GX1, GY1, GX2, GY2 = 12, 12, 138, 278

    def _draw_empty_glass(self):
        c = self.glass
        c.delete("all")
        x1, y1, x2, y2 = self.GX1, self.GY1, self.GX2, self.GY2
        c.create_rectangle(x1, y1, x2, y2, fill=BG_PANEL, outline="#555577", width=2)
        c.create_line(x1+5, y1+8, x1+5, y2-8, fill="#ffffff", width=1, stipple="gray25")
        c.create_text(75, 148, text="🍹",
                      font=font.Font(family="Segoe UI Emoji", size=36), fill=TEXT_DIM)
        wait_text = self.T("waiting")
        c.create_text(75, 290, text=wait_text,
                      font=self.f_small, fill=TEXT_DIM, anchor="center")

    def _draw_glass_filled(self, color, emoji, name, step, total=26):
        c = self.glass
        c.delete("all")
        frac = min(step / total, 1.0)
        x1, y1, x2, y2 = self.GX1, self.GY1, self.GX2, self.GY2
        inner_h = y2 - y1
        c.create_rectangle(x1, y1, x2, y2, fill=BG_PANEL, outline="")
        fill_top = max(y1 + 2, y2 - frac * inner_h)
        if frac > 0:
            c.create_rectangle(x1+2, fill_top, x2-2, y2-2, fill=color, outline="")
        if frac > 0.35:
            for _ in range(8):
                bx = random.randint(x1+8, x2-8)
                by = min(int(fill_top) + random.randint(1, 12), y2-8)
                br = random.randint(2, 5)
                c.create_oval(bx-br, by-br, bx+br, by+br,
                              fill=self._lighten(color, 65), outline="", stipple="gray25")
        if frac > 0.7:
            for (bx, by) in [(22, y2-38), (68, y2-58), (98, y2-32)]:
                if by > int(fill_top) + 4:
                    c.create_rectangle(bx, by, bx+16, by+16,
                                       fill=self._lighten(color, 90),
                                       outline="white", width=1, stipple="gray50")
        if frac > 0.05:
            c.create_line(x1+6, fill_top+4, x1+6, y2-8,
                          fill="white", width=2, stipple="gray50")
        c.create_rectangle(x1, y1, x2, y2, fill="", outline="#8888bb", width=2)
        emoji_size = 38 if frac < 0.55 else 26
        emoji_y = min(max(y1 + max(30, int((y2-y1)*(1-frac)*0.48)), y1+30), y2-30)
        c.create_text(75, emoji_y, text=emoji,
                      font=font.Font(family="Segoe UI Emoji", size=emoji_size),
                      fill=TEXT_MAIN)
        if step >= total:
            c.create_text(75, 290, text=name[:20],
                          font=font.Font(family="Georgia", size=8, slant="italic"),
                          fill=TEXT_DIM, anchor="center")
        if step < total:
            self.root.after(22, lambda: self._draw_glass_filled(
                color, emoji, name, step+1, total))

    def _lighten(self, hex_color, amt=40):
        h = hex_color.lstrip("#")
        r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
        return f"#{min(255,r+amt):02x}{min(255,g+amt):02x}{min(255,b+amt):02x}"

    def _anim_score(self, pct, color, step=0, total=20):
        c = self.score_bar
        c.delete("all")
        w = c.winfo_width() or 260
        cur = (step / total) * pct * (w - 10)
        c.create_rectangle(5, 4, w-5, 18, fill=BG_DARK, outline=BORDER)
        if cur > 0:
            c.create_rectangle(5, 4, 5+cur, 18, fill=color, outline="")
        c.create_text(w//2, 11, text=self.T("match_pct").format(int(pct*100)),
                      font=self.f_small, fill=TEXT_MAIN)
        if step < total:
            self.root.after(28, lambda: self._anim_score(pct, color, step+1, total))

    # ── Generate ───────────────────────────────────────────────────────────────
    def _generate(self):
        prefs = {k: v.get() for k, v in self.vars.items()}
        if sum(prefs.values()) == 0:
            self.lbl_name.config(text=self.T("warn_empty"), fg="#ff6b6b")
            return

        caf = prefs["caffeine"]; frt = prefs["fruit"]
        spc = prefs["spice"];    ref = prefs["refreshment"]
        swt = prefs["sweet"];    sur = prefs["sour"]
        L   = self.lang

        # ── İçecek ───────────────────────────────────────────────────────────
        bev_pool = list(BEVERAGES[caf])

        if self.chk_sparkling.get():
            # Gazlı seçeneği: Gazoz ve Kola'ya öncelik ver
            sk = ["gazoz","cola","sprite","fanta","ginger","soda",
                  "sparkling","tonik","tonic","limonata","lemon soda","portakallı"]
            f = [x for x in bev_pool if any(k in (x[0]+x[1]).lower() for k in sk)]
            if f: bev_pool = f

        if self.chk_warm.get() and caf >= 3:
            warm_bev = ["kahve","coffee","çay","tea","espresso"]
            wb = [x for x in bev_pool if any(k in (x[0]+x[1]).lower() for k in warm_bev)]
            if wb: bev_pool = wb

        beverage = weighted_choice_bilingual(bev_pool, L)

        # ── Meyve ─────────────────────────────────────────────────────────────
        fruit = get_ingredient(FRUITS, frt, L, 0.82)

        # ── Baharat ───────────────────────────────────────────────────────────
        if spc == 0:
            spice = None if random.random() < 0.85 else get_ingredient(SPICES, 1, L, 0.0)
        else:
            pool = list(SPICES[spc])
            if self.chk_warm.get():
                # Sıcak: hibiskus, tarçın, karanfil, kakule, karabaş ağırlıklı
                wk = ["tarçın","cinnamon","kakule","cardamom","karanfil","clove",
                      "hibiskus","hibiscus","zencefil","ginger","zerdeçal","turmeric",
                      "anason","anise"]
                wp = [x for x in pool if any(k in (x[0]+x[1]).lower() for k in wk)]
                if wp: pool = wp
            if self.chk_bold.get() and spc >= 3:
                bk = ["acı","chili","karabiber","pepper","jalapeño"]
                bp = [x for x in pool if any(k in (x[0]+x[1]).lower() for k in bk)]
                if bp: pool = bp
            spice = weighted_choice_bilingual(pool, L)

        # ── Ferahlık ──────────────────────────────────────────────────────────
        ref_val = max(ref, 3) if self.chk_light.get() else ref
        refreshment = get_ingredient(REFRESHMENTS, ref_val, L, 0.80)

        # Sıcak seçeneği seçiliyse buz içeren ferahlık malzemelerini filtrele
        if self.chk_warm.get() and refreshment:
            ice_words = ["buz","ice","crushed","kırık","mentol","menthol"]
            if any(k in refreshment.lower() for k in ice_words):
                # Buzsuz bir seçenek bul
                no_ice = [x for x in (REFRESHMENTS.get(ref_val) or REFRESHMENTS.get(max(1,ref_val-1)) or [])
                          if not any(k in (x[0]+x[1]).lower() for k in ice_words)]
                if no_ice:
                    refreshment = weighted_choice_bilingual(no_ice, L)

        # ── Ekstra ───────────────────────────────────────────────────────────
        if swt > sur + 1:   extra = weighted_choice_bilingual(EXTRAS_SWEET, L)
        elif sur > swt + 1: extra = weighted_choice_bilingual(EXTRAS_SOUR, L)
        else:               extra = weighted_choice_bilingual(EXTRAS_NEUTRAL, L)

        # Sıcak seçeneği: ekstra'da buz olmasın
        if self.chk_bold.get():
            # Yoğun & Güçlü → vanilya, karamel, yoğun meyve şurupları
            bold_extras_tr = [
                "Vanilya Şurubu (Çift)",
                "Karamel Şurubu",
                "Çilek Şurubu",
                "Ahududu Şurubu",
                "Böğürtlen Şurubu",
                "Mango Şurubu",
                "Nar Şurubu",
                "Karamel + Vanilya",
                "Yoğun Hibiskus Şurubu",
            ]
            bold_extras_en = [
                "Double Vanilla Syrup",
                "Caramel Syrup",
                "Strawberry Syrup",
                "Raspberry Syrup",
                "Blackberry Syrup",
                "Mango Syrup",
                "Pomegranate Syrup",
                "Caramel + Vanilla",
                "Intense Hibiscus Syrup",
            ]
            if L == "TR":
                extra = random.choice(bold_extras_tr)
            else:
                extra = random.choice(bold_extras_en)
        if self.chk_warm.get():
            ice_extras = ["buz","ice","kırık","crushed"]
            if any(k in extra.lower() for k in ice_extras):
                extra = {"TR": "Tarçın Garnisi", "EN": "Cinnamon Stick"}[L]

        # ── Kategori & isim ───────────────────────────────────────────────────
        if caf >= 4:   cat = "dark_spicy" if spc >= 3 else "dark_fruity"
        elif spc >= 4: cat = "light_spicy"
        elif frt >= 4 and spc <= 1: cat = "light_fruity"
        elif 2 <= spc <= 3 and frt >= 2:
            cat = "light_floral" if swt >= 3 else "refreshing"
        elif ref >= 3 and spc <= 2: cat = "refreshing"
        elif swt >= 4 and sur <= 1: cat = "sweet_creamy"
        elif sur >= 4: cat = "citrus_sour"
        else: cat = "default"

        pool = COCKTAIL_NAMES[cat]
        available = [t for t in pool if t[0] != self._last_name]
        if not available: available = pool
        name, color, emoji = random.choice(available)
        self._last_name = name

        # ── Alternatifler ─────────────────────────────────────────────────────
        alt_cats = [c for c in COCKTAIL_NAMES if c != cat]
        random.shuffle(alt_cats)
        alternatives = [random.choice(COCKTAIL_NAMES[c]) for c in alt_cats[:4]]

        # ── Açıklama ─────────────────────────────────────────────────────────
        bev_s = beverage
        fr_s  = fruit       or bev_s
        sp_s  = spice       or ""
        ref_s = refreshment or bev_s
        tmpl  = random.choice(self.T("desc_templates"))
        description = tmpl.format(bev=bev_s, fr=fr_s.lower(),
                                   sp=sp_s.lower(), ref=ref_s.lower())

        # ── Eşleşme skoru ─────────────────────────────────────────────────────
        active = sum(1 for v in prefs.values() if v > 0)
        high   = sum(1 for v in prefs.values() if v >= 3)
        pct = min(0.50 + (active/6)*0.25 + (high/6)*0.20
                  + random.uniform(-0.03, 0.05), 0.99)

        # ── UI ────────────────────────────────────────────────────────────────
        self._draw_glass_filled(color, emoji, name, step=0)
        self.lbl_name.config(text=name, fg=color)
        self.lbl_desc.config(text=description, fg=TEXT_MAIN)

        for w in self.ing_frame.winfo_children(): w.destroy()
        labels = self.T("ing_labels")
        ing_data = list(zip(
            labels,
            [beverage, fruit, spice, refreshment, extra],
            [FLAVOR_COLORS[k] for k in ["caffeine","fruit","spice","refreshment","sweet"]]
        ))
        for cat_lbl, item, col in ing_data:
            if not item: continue
            row = tk.Frame(self.ing_frame, bg=BG_CARD)
            row.pack(fill=tk.X, pady=1)
            tk.Label(row, text="●", font=self.f_small,
                     bg=BG_CARD, fg=col).pack(side=tk.LEFT, padx=(0,4))
            tk.Label(row, text=f"{cat_lbl}:", font=self.f_small,
                     bg=BG_CARD, fg=TEXT_DIM, width=10, anchor="w").pack(side=tk.LEFT)
            tk.Label(row, text=item, font=self.f_body,
                     bg=BG_CARD, fg=TEXT_MAIN).pack(side=tk.LEFT)

        self.root.after(80, lambda: self._anim_score(pct, color))

        # ── Tek öneri — yan kutu ──────────────────────────────────────────
        for w in self.runner_frame.winfo_children(): w.destroy()
        if alternatives:
            aname, acolor, aemoji = alternatives[0]
            row = tk.Frame(self.runner_frame, bg=BG_CARD)
            row.pack(fill=tk.X, pady=1)
            dot = tk.Canvas(row, width=10, height=10, bg=BG_CARD, highlightthickness=0)
            dot.create_oval(1,1,9,9, fill=acolor, outline="")
            dot.pack(side=tk.LEFT, padx=(0,4))
            tk.Label(row, text=f"{aemoji} {aname}", font=self.f_small,
                     bg=BG_CARD, fg=TEXT_DIM).pack(side=tk.LEFT)

        # Yan öneri kutusu — farklı kategori
        if len(alternatives) > 1:
            sname, scolor, semoji = alternatives[1]
            self.suggest_name_lbl.config(
                text=f"{semoji}  {sname}", fg=scolor)
        elif alternatives:
            sname, scolor, semoji = alternatives[0]
            self.suggest_name_lbl.config(
                text=f"{semoji}  {sname}", fg=scolor)

    def _open_wiki(self, event=None):
        import webbrowser
        webbrowser.open(f"https://en.wikipedia.org/wiki/{self._current_wiki}")

    def _open_youtube(self, event=None):
        import webbrowser
        webbrowser.open("https://www.youtube.com/@dogancanozgokceler3234")

    # ── Reset ──────────────────────────────────────────────────────────────────
    def _reset(self):
        for v in self.vars.values(): v.set(0)
        for lbl in self.val_labels.values(): lbl.config(text="0")
        for var in (self.chk_sparkling, self.chk_warm, self.chk_light, self.chk_bold):
            var.set(False)
        self._draw_empty_glass()
        self.lbl_name.config(text=self.T("placeholder"), fg=TEXT_DIM)
        self.lbl_desc.config(text="")
        for w in self.ing_frame.winfo_children(): w.destroy()
        for w in self.runner_frame.winfo_children(): w.destroy()
        self.score_bar.delete("all")

    def _hover(self, btn, normal, hover):
        btn.bind("<Enter>", lambda _: btn.config(bg=hover))
        btn.bind("<Leave>", lambda _: btn.config(bg=normal))

    def _start_animations(self):
        self._anim_bubbles()
        self._anim_title()

    def _anim_bubbles(self):
        c = self.bub_canvas
        c.delete("all")
        for b in self.bubbles:
            b.step()
            c.create_oval(b.x-b.r, b.y-b.r, b.x+b.r, b.y+b.r,
                          fill=b.color, outline="", stipple="gray50")
        self.root.after(38, self._anim_bubbles)

    def _anim_title(self, tick=0):
        colors = [TEXT_MAIN,"#ffd93d","#ffe8a0","#ffd93d",TEXT_MAIN,
                  "#6bcb77",TEXT_MAIN,"#4d96ff",TEXT_MAIN]
        self.hdr.itemconfig(self.title_id, fill=colors[tick % len(colors)])
        self.root.after(700, lambda: self._anim_title(tick+1))


if __name__ == "__main__":
    root = tk.Tk()
    app = CocktailApp(root)
    root.mainloop()
