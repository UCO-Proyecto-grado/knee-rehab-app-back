import httpx

async def post_token_exchange(url: str, data: dict, headers: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data, headers=headers)
        response.raise_for_status()
        return response.json()
