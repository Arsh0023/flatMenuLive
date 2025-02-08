class Dish:
    def __init__(self, name, link, region):
        self.name = name
        self.link = link
        self.region = region

    def __repr__(self):
        return f'{self.name}'
    
#Dishes Menu
north_indian_vegetarian_dishes = [
    "Paneer Butter Masala",    # Rich cottage cheese in tomato-cream sauce [1][2][10]
    "Chole",                    # Spiced chickpea curry with bhatura [1][2][17]
    "Palak Paneer",             # Spinach and cottage cheese curry [1][2][10]
    "Aloo Tamatar ki Sabzi",    # Potato-tomato curry [1][2]
    "Dal Tadka",                # Tempered lentil dish [1][10][17]
    "Bhindi Masala",            # Spiced okra sauté [1][2]
    "Aloo Gobi",                # Potato-cauliflower dry curry [1][4][10]
    "Karela Sabzi",             # Bitter gourd stir-fry [1][2]
    "Rajma",                    # Kidney bean curry [1][2][10]
    "Malai Kofta",              # Cottage cheese dumplings in creamy sauce [1][10][12]
    "Baingan Bharta",           # Smoky roasted eggplant mash [1][2]
    "Chana Masala",             # Spicy chickpea curry [1][4][10]
    "Dal Makhani",              # Creamy black lentil curry [3][10][17]
    "Navratan Korma",           # Mixed vegetable curry in cashew sauce [1][4]
    "Sarson ka Saag",           # Mustard greens curry [15][17]
    "Shahi Paneer",             # Royal cottage cheese in rich gravy [10][17]
    "Methi Malai Mutter",       # Fenugreek-peas cream curry [4][15]
    "Kadhi Pakora",             # Yogurt gravy with fried dumplings [17]
    "Aloo Paratha",             # Stuffed potato flatbread [3][17]
    "Vegetable Biryani",        # Spiced rice with mixed vegetables [13]
    "Gajar Ka Halwa",           # Carrot-based sweet dessert [17]
    "Dahi Bhalla",              # Lentil dumplings in yogurt [3][12]
    "Samosa",                   # Spiced potato stuffed pastry [3][17]
    "Punjabi Kadhi",            # Spiced yogurt-based curry [17]
    "Lauki Kofta",              # Bottle gourd dumplings in gravy [17]
    "Sarso ka Saag",            # Mustard greens with makki roti [15]
    "Matar Paneer",             # Peas and cottage cheese curry [17]
    "Shalgam ki Sabzi",         # Spiced turnip curry [13]
    "Kachori",                  # Flaky stuffed pastry [12]
    "Gobi Paratha"              # Cauliflower-stuffed flatbread [17]
]