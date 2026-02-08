from escale_ai.agent_factory import AgentFactory


def main():
    # Run the base pipeline and print results
    base_results = AgentFactory.run_base_pipeline()
    print("Base Pipeline Results:")
    print(base_results)

    # Run a client pipeline for a demo client and print results
    client_results = AgentFactory.run_client_pipeline("Demo Clinic")
    print("Client Pipeline Results:")
    print(client_results)


if __name__ == "__main__":
    main()
