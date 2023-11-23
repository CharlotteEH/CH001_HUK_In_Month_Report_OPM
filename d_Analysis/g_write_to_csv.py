from f_extract_lists import  list_date, list_market, list_product
from e_ros import wide_results
from pathlib import Path

path = Path("Z:/PycharmProjects/CH001_HUK_In_Month_Report_OPM/d_Analysis")

wide_results.loc[wide_results["product"].isin(["Carlsberg Marston's Brewing Company"]), "product"] = "Carlsberg Marstons Brewing Company"
wide_results = wide_results.query('product in ["Birra Moretti",	"Peroni Nastro Azzurro", "Madri Excepcional", "Estrella Damm",	'
                                  '"Corona Extra", "Staropramen", "Cobra", "Asahi Super Dry", "Angelo Poretti No 3", "Carling",'
                                  '"Fosters", "Carlsberg Danish Pilsner", "Tennents Lager", "Coors", "Stella Artois", "San Miguel",'
                                  '"Amstel", "Kronenbourg 1664", "Pravha", "Bud Light", "Becks 4%", "Heineken Original", "Heineken Silver",'
                                  '"Cruzcampo",	"Beavertown Neck Oil Session IPA", "Camden Town Pale Ale", "John Smiths Extra Smooth",'
                                  '"Worthington Creamflow", "Guinness", "Strongbow", "Thatchers Gold", "Stowford Press",'
                                  '"Inchs", "Magners Original", "Aspall Cyder", "Strongbow Dark Fruit",'
                                  '"Carling Black Fruit Cider",	"Kopparberg (all flavours)", "Rekorderlig (all flavours)", "Old Mout Cider (all flavours)" , "Bulmers (all flavours)",'
                                  '"Magners Dark Fruit","Stowford Press Mixed Berries", "Adnams", "Asahi UK", "Black Sheep","Brewdog",'
                                  '"Budweiser Brewing Group UK&I", "Butcombe", "C & C Group", "Carlsberg Marstons Brewing Company",'
                                  '"Diageo GB","Harveys","Heineken UK","Hogs Back","Innis & Gunn","Molson Coors", "SA Damm","St Austell",'
                                  '"Thatchers","Theakstons","Timothy Taylor","Tiny Rebel","Westons"]')


list_date.to_csv(path / "list_date.csv", index=False)
list_market.to_csv(path / "list_market.csv", index=False)
list_product.to_csv(path / "list_product.csv", index=False)

wide_results.to_csv(path / "wide_results.csv", index=False)