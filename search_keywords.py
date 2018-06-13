""" Compile publication data for astronomy journals over the last 60 years. """

import json
import ads

if __name__ == "__main__":
    years = (1947, 2017)
    keywords = ["for the first time", "novel", "excellent", "robust", "unique", "unprecedented", "promising", "remarkable", "encouraging", "enormous", "cutting-edge","state-of-the-art","preeminent"]

    journals = [# (Scraped from Wikipedia)
        "Astronomical Journal",
        "Astronomy and Astrophysics",
        "The Astrophysical Journal",
        "The Astrophysical Journal Letters",
        "The Astrophysical Journal Supplement Series",
        "Journal of Cosmology and Astroparticle Physics",
        "Monthly Notices of the Royal Astronomical Society",
        "Publications of the Astronomical Society of Japan",
        "Publications of the Astronomical Society of the Pacific"]

    bibstemlist = ["AJ", "ApJ", "A&A", "MNRAS", "PASP", "PASJ", "PhRvD", "JCAP"]

    for keyword in keywords:
        print(keyword)
    
        publication_data = []
    
        for journal in bibstemlist:
            # Initiate the dictionary for this journal
            journal_data = {
                "name": journal,
                "articles": [],
                "total": 0
            }

            for year in range(years[0], years[1] + 1):
                # Perform the query
                # We actually don't want all the results, we just want the metadata
                # which tells us how many publications there were
                q = ads.SearchQuery(q="abstract:(=\"{keyword}\") bibstem:\"{journal}\" year:{year}".format(keyword=keyword, journal=journal, year=year), fl=['id'], rows=1)
                q.execute()
                
                num = int(q.response.numFound)
                print("using {keyword} in abstract {journal} had {num} publications in {year}"
                      .format(keyword=keyword, journal=journal, num=num, year=year))

                # Save this data
                journal_data["articles"].append([year, num])
                journal_data["total"]   += num

            # Let's only save it if there were actually any publications
            if journal_data["total"] > 0:
                    publication_data.append(journal_data)

            sorted_publication_data = []
            totals = [journal["total"] for journal in publication_data]
            indices = sorted(range(len(totals)),key=totals.__getitem__)
            for index in indices:
                sorted_publication_data.append(publication_data[index])
            
            # Save the data
            with open(keyword+'journal-publications-keywords.json', 'w') as fp:
                json.dump(sorted_publication_data, fp, indent=2)
