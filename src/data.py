import requests
from bs4 import BeautifulSoup

def get_data(pos, plr):
    # Select appropriate page from position
    pos_to_page = {
        1: "qb.php",
        2: "rb.php",
        3: "wr.php",
        4: "te.php",
        5: "k.php",
        6: "dst.php",
        7: "dl.php",
        8: "lb.php",
        9: "db.php"
    }

    url_end = pos_to_page[pos]

    for year in range(2025, 2001, -1):
        url = "https://www.fantasypros.com/nfl/stats/"+url_end+f"?year={year}"
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table", id="data")
        rows = table.find_all("tr")

        for row in rows[2:]:
            cells = row.find_all("td")
            name = cells[1].get_text(strip=True)

            # Remove team from player name
            name = name.split('(')[0]

            if name.lower() == plr.lower():
                fpts = float(cells[15].get_text(strip=True))
                print(name, fpts)

                # player has been found, exit loop
                break
        
        # Player wasn't found, gets 0 for the year
        print(name, 0)
        
    print(pos)
    print(plr)