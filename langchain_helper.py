from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from secrete import openai_key

import os
os.environ['OPENAI_API_KEY'] = openai_key

llm = OpenAI(temperature = 0.7)

def generate_restaurant_names_and_menu_items(cuisine):
    # Chain-1
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_name,
        output_key="restaurant_name"
    )

    # Chain-2
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest me some food menu items for {restaurant_name}."
    )

    food_items_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_items,
        output_key="menu_items"
    )

    # Sequential Chain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=["cuisine"],  # Initial input
        output_variables=["restaurant_name", "menu_items"]  # Final outputs
    )

    # Run the chain
    result = chain({'cuisine': cuisine})
    return result

# if __name__ == "__main__":
#     print(generate_restaurant_names_and_menu_items("Indian"))