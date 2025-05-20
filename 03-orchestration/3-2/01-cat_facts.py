import httpx
from prefect import flow, task



# This api calls a fact about cat
@task(retries=4, 
      retry_delay_seconds=0.1, 
      log_prints=True # any print within the task will be shared within logs
      )
def fetch_cat_fact():
    cat_fact = httpx.get("https://f3-vyx5c2hfpq-ue.a.run.app/")
    #An endpoint that is designed to fail sporadically
    if cat_fact.status_code >= 400:
        raise Exception()
    print(cat_fact.text)


@flow
def fetch():
    fetch_cat_fact()


if __name__ == "__main__":
    fetch()