import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Arshad561/f6f4f88ca391f68830bb67e6bf0ac538/raw/2dd03b2245c2796c01c26ce0824e14a87d42f830/arshad-shaik.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_key = os.environ.get("PROXYCURL_API_KEY")
        headers = {"Authorization": "Bearer " + api_key}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {
            "linkedin_profile_url": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            headers=headers,
            timeout=10,
        )

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/arshad-basha-shaik-2085a0129/",
            mock=True,
        )
    )
