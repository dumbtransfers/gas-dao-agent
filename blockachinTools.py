import requests
from phi.tools import Toolkit

class BlockchainTools(Toolkit):
    def __init__(self):
        super().__init__(name="blockchain_tools")
        self.register(self.get_gas_fee)

    def get_gas_fee(self, blockchain="ethereum"):
        # Replace with actual API endpoint
        api_url = f"https://api.example.com/gas-fee/{blockchain}"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()["gas_fee"]
        else:
            return "Failed to fetch gas fee"