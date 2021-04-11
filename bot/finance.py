import requests
import random
import discord
# polygon API


# get stock data based on ticker
def getTicker(ticker, apiKey):
        data =requests.get(f"https://api.polygon.io/v1/meta/symbols/{ticker}/company?&apiKey={apiKey}")
        msg = ""
        if data.status_code == 200:
                msg += "Company Name: "+data.json()['name'] +"\n"
                msg += "Location: "+data.json()['hq_address'] +"\n"
                msg += "Industry: "+data.json()['industry'] +"\n"
                msg += "Sector: "+data.json()['sector'] +"\n"
                msg += "Description: "+data.json()['description'] +"\n"
                msg += "Market Cap: $"+str(data.json()['marketcap']) +" USD\n"
                msg += "Employees: "+str(data.json()['employees']) +"\n"
                msg += "Phone: "+data.json()['phone'] +"\n"
                msg += "CEO: "+data.json()['ceo'] +"\n"
                msg += "URL: "+data.json()['phone'] +"\n"
                msg += "Exchange: "+data.json()['exchange'] +"\n"
                msg += "List date: " +data.json()['listdate'] +"\n"
                msg += "Bloomberg: "+data.json()['bloomberg'] +"\n"
                msg += "lei: "+str(data.json()['lei']) +"\n"
                msg += "sic: "+str(data.json()['sic']) +"\n"
                msg += "Country: "+data.json()['country'] +"\n"
                msg += "Updated: "+ data.json()['updated']+"\n"
                tags = ""
                for t in data.json()['tags']:
                        tags+= t+", "
                msg += "Tags: " + tags+"\n"
                similar = ""
                for s in data.json()['similar']:
                        similar += s+", "
                msg += "Similar: "+ similar + "\n"
                msg += "Data provided by polygon.io\n"
        else:
                msg = "Invalid stock ticker."
        return msg
# get news based on stock ticker
def tickerNews(ticker, apiKey):
        data =requests.get(f"https://api.polygon.io/v1/meta/symbols/{ticker}/news?perpage=50&page=1&apiKey={apiKey}")        
        if data.status_code == 200:
                i = random.randint(0,50)
                embed = discord.Embed(title=data.json()[i]['title'],url=data.json()[i]['url'],description=data.json()[i]['summary'],color=discord.Color.red())
                embed.add_field(name="Source:",value=data.json()[i]['source'],inline=False )
                embed.set_footer(text=data.json()[i]['timestamp'])
                return embed

