import PricingFunctions
import time

query = "Hello! What are tokens and how are they calculated?"
llm_response = "Tokens can be anything from words, character sets, or even combinations of words and punctuation. Each model calculates them differently according to its own set of rules."


PricingFunctions.anthropic_pricing(query, llm_response, "claude opus 4")

PricingFunctions.anthropic_pricing(query, llm_response, "Claude Sonnet 4")

PricingFunctions.openai_pricing(query, llm_response, "GPT-4.1")
PricingFunctions.openai_pricing(query, llm_response, "openaio3")


query2 = "How many days are there in a year?"
llm_response2 = "There are 365 days in a year, but every 4 years a leap year comes around which has 366 days instead."


PricingFunctions.anthropic_pricing(query2, llm_response2, "claude opus 4")

PricingFunctions.anthropic_pricing(query2, llm_response2, "Claude Sonnet 4")

PricingFunctions.openai_pricing(query2, llm_response2, "GPT-4.1")
PricingFunctions.openai_pricing(query2, llm_response2, "openaio3")


print("Wait for 2 mins to test if time is being logged properly")
time.sleep(120)
print('Starting...\n\n\n')


query3 = "Hello! What are tokens and how are they calculated?"
llm_response3 = "Tokens can be anything from words, character sets, or even combinations of words and punctuation. Each model calculates them differently according to its own set of rules."


PricingFunctions.anthropic_pricing(query3, llm_response3, "claude opus 4")

PricingFunctions.anthropic_pricing(query3, llm_response3, "Claude Sonnet 4")

PricingFunctions.openai_pricing(query3, llm_response3, "GPT-4.1")
PricingFunctions.openai_pricing(query3, llm_response3, "openaio3")



PricingFunctions.print_log(PricingFunctions.claude_opus4_memlog)
PricingFunctions.print_log(PricingFunctions.claude_sonnet4_memlog)
PricingFunctions.print_log(PricingFunctions.gpt4_1_memlog)
PricingFunctions.print_log(PricingFunctions.openaio3_memlog)