from zenpy import Zenpy
import json
from html2text import html2text

# Create a Zenpy instance
zenpy_client = Zenpy(
    **dict(
        email="jose.fonte@cloudbeds.com",
        token="bITFylYd61HdPESyE7V1GhdwOYLW1vxOStSMtXBE",
        subdomain="cloudbeds",
    )
)

# Get all KB articles
articles = zenpy_client.help_center.articles()
list_of_articles = []


def dump_to_single_file(articles):
    first = True
    with open(f"all.json", "w") as f:
        for article in articles:
            if "internal" in article.title.lower():
                # print(f"Skipping {article.title}")
                continue
            if first:
                f.write("[")
                first = False
            else:
                f.write(",\n")
            temp = dict(
                id=article.id,
                text=html2text(article.body),
                source="file",
                source_id=article.url,
                url=article.url,
                created_at=article.created_at,
                author=article.author_id,
            )
            f.write(json.dumps(temp, indent=4))
        f.write("]")


def dump_to_multiple_files(articles, limit=100):
    i = 0
    count = 0
    first = True
    for article in articles:
        with open(f"all-{i}.json", "a+") as f:
            if "internal" in article.title.lower():
                # print(f"Skipping {article.title}")
                continue
            if first:
                f.write("[")
                first = False
            else:
                f.write(",\n")
            temp = dict(
                id=article.id,
                text=html2text(article.body),
                source="file",
                source_id=article.url,
                url=article.url,
                created_at=article.created_at,
                author=article.author_id,
            )
            f.write(json.dumps(temp, indent=4))
            count += 1
            if count >= limit:
                f.write("]")
                first = True
                count = 0
                print(f"Finished file {i}")
                i += 1
                continue

    with open(f"all-{i}.json", "a+") as f:
        f.write("]")
