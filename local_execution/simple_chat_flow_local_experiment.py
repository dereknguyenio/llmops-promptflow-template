from dotenv import load_dotenv 
load_dotenv()  

from prompt_experimentation.run_local import LocalFlowExecution

def main():
    data = "simple_chat_flow/data/data.jsonl"
    flow = "simple_chat_flow/flows/standard"
    eval_flow = "simple_chat_flow/flows/evaluation"
    simple_chat_flow = LocalFlowExecution(flow, eval_flow, data, {"question": "${data.question}"})
    simple_chat_flow.process_local_flow()
    simple_chat_flow.create_local_connections()
    run_ids = simple_chat_flow.execute_experiment()

    simple_chat_flow.execute_evaluation(run_ids,data,{
                "question": "${data.question}",
                "answer": "${run.outputs.answer}",
            })

if __name__ == "__main__":
    main()