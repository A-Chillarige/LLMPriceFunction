
from dataclasses import dataclass, field
import tiktoken
from datetime import datetime

query = "Hello! What are tokens and how are they calculated?"
llm_response = "Tokens can be anything from words, character sets, or even combinations of words and punctuation. Each model calculates them differently according to its own set of rules."


@dataclass(slots = True) # slots helps save memory
class Memory:
    query: str
    query_tokens: int
    query_cost: float
    llm_response: str
    response_tokens: int
    response_cost: float
    total_cost: float
    time: list[datetime] = field(default_factory = list)  # the field(default_factory...) part is used to ensure each instance of Memory has its own list

claude_opus4_memlog = {}
claude_sonnet4_memlog = {}
gpt4_1_memlog = {}
openaio3_memlog = {}


def tokenizer (query, llm_response, model):
    """
    This function taken in input text(user query), the llm response and the model the you're using and calculates the tokens in each statement

    >>> query = "Hello! What are tokens and how are they calculated?"
    >>> llm_response = "Tokens can be anything from words, character sets, or even combinations of words and punctuation. Each model calculates them differently according to its own set of rules."
    >>> query_tokens, response_tokens, model = tokenizer(query, llm_response, 'Claude Opus 4')
    >>> print(query_tokens, response_tokens, model)
    11 31 claudeopus4

    >>> query_tokens, response_tokens, model = tokenizer(query, llm_response, 'Claude Sonnet 4')
    >>> print(query_tokens, response_tokens, model)
    11 31 claudesonnet4

    >>> query_tokens, response_tokens, model = tokenizer(query, llm_response, 'GPT-4.1')
    >>> print(query_tokens, response_tokens, model)
    11 31 gpt-4.1

    >>> query_tokens, response_tokens, model = tokenizer(query, llm_response, 'openaio3')
    >>> print(query_tokens, response_tokens, model)
    11 31 openaio3

    >>> query_tokens, response_tokens, model = tokenizer(query, llm_response, 'openai03')
    Unknown Model. Please try again
    >>> print(query_tokens, response_tokens, model)
    0 0 Unknown Model
    
    """
    model = model.replace(" ", "").lower()

    if model == 'claudeopus4' or model == 'claudesonnet4':
        enc = tiktoken.get_encoding("cl100k_base")
    elif model == 'gpt-4.1' or model == 'openaio3':
        enc = tiktoken.encoding_for_model('o3-12k')
    else:
        print("Unknown Model. Please try again")
        return 0, 0, 'Unknown Model'

    
    query_tokens = enc.encode(query)
    response_tokens = enc.encode(llm_response)


    return len(query_tokens), len(response_tokens), model


def anthropic_pricing(query, llm_response, model = 'claude opus 4'):

    global claude_opus4_memlog 
    global claude_sonnet4_memlog 

    query_tokens, response_tokens, model = tokenizer(query, llm_response, model)

    if model == 'claudeopus4':

        if query not in claude_opus4_memlog:

            query_cost = query_tokens * (18.75/1000000)
            response_cost = response_tokens * (75/1000000)
            total_cost = query_cost + response_cost

            print("You used {} tokens in your query. The cost was: ${}\nThe llm response used {} tokens. The cost was: ${}".format(query_tokens, query_cost, response_tokens, response_cost))
            print("Total cost was: ${}".format(total_cost))
            print('\n')

            claude_opus4_memlog[query] = Memory(
                query = query,
                query_tokens = query_tokens,
                query_cost = query_cost,
                llm_response = llm_response,
                response_tokens = response_tokens,
                response_cost = response_cost,
                total_cost = total_cost,
            )
            time = datetime.now()
            claude_opus4_memlog[query].time.append(time)
      
        else:

            query_retrieval_cost = claude_opus4_memlog[query].query_tokens * (1.5/1000000)
            response_cost = 0
            claude_opus4_memlog[query].total_cost += query_retrieval_cost
            time = datetime.now()
            claude_opus4_memlog[query].time.append(time)

            print("You have used this query before! You used {} tokens in your query. The retrieval cost is: ${}\nThe llm response used {} tokens. The cost is: ${}".format(claude_opus4_memlog[query].query_tokens, query_retrieval_cost, claude_opus4_memlog[query].response_tokens, response_cost))
            print("New total cost is: ${}".format(claude_opus4_memlog[query].total_cost))   
            print('\n')

    elif model == 'claudesonnet4':

        if query not in claude_sonnet4_memlog:

            query_cost = query_tokens * (3.75/1000000)
            response_cost = response_tokens * (15/1000000)
            total_cost = query_cost + response_cost

            print("You used {} tokens in your query. The cost was: ${}\nThe llm response used {} tokens. The cost was: ${}".format(query_tokens, query_cost, response_tokens, response_cost))
            print("Total cost was: ${}".format(total_cost))
            print('\n')

            claude_sonnet4_memlog[query] = Memory(
                query = query,
                query_tokens = query_tokens,
                query_cost = query_cost,
                llm_response = llm_response,
                response_tokens = response_tokens,
                response_cost = response_cost,
                total_cost = total_cost,
            )
            time = datetime.now()
            claude_sonnet4_memlog[query].time.append(time)
       
        else:

            query_retrieval_cost = claude_sonnet4_memlog[query].query_tokens * (1.5/1000000)
            response_cost = 0
            claude_sonnet4_memlog[query].total_cost += query_retrieval_cost
            time = datetime.now()
            claude_sonnet4_memlog[query].time.append(time)

            print("You have used this query before! You used {} tokens in your query. The cost is: ${}\nThe llm response used {} tokens. The cost is: ${}".format(claude_sonnet4_memlog[query].query_tokens, query_retrieval_cost, claude_sonnet4_memlog[query].response_tokens, response_cost))
            print("New total cost is: ${}".format(claude_sonnet4_memlog[query].total_cost))
            print('\n')

    else:
        print("Unknown Model! Please try again.")

        return None


def openai_pricing(query, llm_response, model = 'GPT-4.1'):

    global gpt4_1_memlog 
    global openaio3_memlog 

    query_tokens, response_tokens, model = tokenizer(query, llm_response, model)

    if model == 'gpt-4.1': 

        if query not in gpt4_1_memlog:

            query_cost = query_tokens * (2/1000000)
            response_cost = response_tokens * (8/1000000)
            total_cost = query_cost + response_cost

            print("You used {} tokens in your query. The cost was: ${}\nThe llm response used {} tokens. The cost was: ${}".format(query_tokens, query_cost, response_tokens, response_cost))
            print("Total cost was: ${}".format(total_cost))
            print('\n')

            gpt4_1_memlog[query] = Memory(
                query = query,
                query_tokens = query_tokens,
                query_cost = query_cost,
                llm_response = llm_response,
                response_tokens = response_tokens,
                response_cost = response_cost,
                total_cost = total_cost,
            )
            time = datetime.now()
            gpt4_1_memlog[query].time.append(time)

        else:

            query_retrieval_cost = gpt4_1_memlog[query].query_tokens * (0.5/1000000)
            response_cost = 0
            gpt4_1_memlog[query].total_cost += query_retrieval_cost
            time = datetime.now()
            gpt4_1_memlog[query].time.append(time)

            print("You have used this query before! You used {} tokens in your query. The cost is: ${}\nThe llm response used {} tokens. The cost is: ${}".format(gpt4_1_memlog[query].query_tokens, query_retrieval_cost, gpt4_1_memlog[query].response_tokens, response_cost))
            print("New total cost is: ${}".format(gpt4_1_memlog[query].total_cost))
            print('\n')

    elif model == 'openaio3':

        if query not in openaio3_memlog: 

            query_cost = query_tokens * (2/1000000)
            response_cost = response_tokens * (8/1000000)
            total_cost = query_cost + response_cost

            print("You used {} tokens in your query. The cost was: ${}\nThe llm response used {} tokens. The cost was: ${}".format(query_tokens, query_cost, response_tokens, response_cost))
            print("Total cost was: ${}".format(total_cost))
            print('\n')


            openaio3_memlog[query] = Memory(
                query = query,
                query_tokens = query_tokens,
                query_cost = query_cost,
                llm_response = llm_response,
                response_tokens = response_tokens,
                response_cost = response_cost,
                total_cost = total_cost,  
            )
            time = datetime.now()
            openaio3_memlog[query].time.append(time)          

        else:

            query_retrieval_cost = openaio3_memlog[query].query_tokens * (0.5/1000000)
            response_cost = 0
            openaio3_memlog[query].total_cost += query_retrieval_cost
            time = datetime.now()
            openaio3_memlog[query].time.append(time)    

            print("You have used this query before! You used {} tokens in your query. The cost is: ${}\nThe llm response used {} tokens. The cost is: ${}".format(openaio3_memlog[query].query_tokens, query_retrieval_cost, openaio3_memlog[query].response_tokens, response_cost))
            print("New total cost is: ${}".format(openaio3_memlog[query].total_cost))
            print('\n')
   
    else:
        print("Unknown Model! Please try again.")
        print('\n')
   
    return None



def print_log(log):
    print("Printing Log Memory:")
    print("-------------------------------")


    for key, value in log.items():
        print("Query:",value.query)
        print("Number of Tokens in Query :", value.query_tokens)
        print("Query Cost: ${}".format(value.query_cost))
        print("LLM Response:", value.llm_response)
        print("Number of Tokens in Response:", value.response_tokens)
        print("Response Cost: ${}".format(value.response_cost))
        print("Total Cost: ${}".format(value.total_cost))
        print("Time: {}".format(value.time))
        print()

    print("-------------------------------")
    print()

    return None


def clear_all_logs():
    claude_opus4_memlog.clear()
    claude_sonnet4_memlog.clear()
    gpt4_1_memlog.clear()
    openaio3_memlog.clear()

    return None
