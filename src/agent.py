#!/usr/bin/env python3
"""
Production-Ready LangChain AI Agent
Multi-tool capable agent with memory management and extensible architecture
"""

import os
from typing import List, Dict, Any, Optional
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool, tool
from langchain.schema import SystemMessage
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AIAgent:
    """
    Production-ready AI Agent with LangChain integration.
    Features:
    - Multiple tool support
    - Conversation memory
    - Error handling
    - Configurable LLM backend
    """
    
    def __init__(
        self,
        model_name: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: int = 2000
    ):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        # Initialize LLM
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        # Initialize memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Define tools
        self.tools = self._initialize_tools()
        
        # Create agent
        self.agent = self._create_agent()
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True
        )
        
        logger.info(f"AI Agent initialized with model: {model_name}")
    
    def _initialize_tools(self) -> List[Tool]:
        """
        Initialize available tools for the agent.
        """
        return [
            Tool(
                name="Calculator",
                func=self.calculator,
                description="Useful for mathematical calculations"
            ),
            Tool(
                name="TextAnalysis",
                func=self.text_analysis,
                description="Analyze text and provide insights"
            ),
            Tool(
                name="CodeGenerator",
                func=self.code_generator,
                description="Generate code snippets based on requirements"
            )
        ]
    
    @staticmethod
    def calculator(query: str) -> str:
        """
        Simple calculator tool.
        """
        try:
            result = eval(query)
            return f"Result: {result}"
        except Exception as e:
            return f"Error in calculation: {str(e)}"
    
    @staticmethod
    def text_analysis(text: str) -> str:
        """
        Analyze text and provide basic metrics.
        """
        word_count = len(text.split())
        char_count = len(text)
        return f"Analysis: {word_count} words, {char_count} characters"
    
    @staticmethod
    def code_generator(requirements: str) -> str:
        """
        Generate simple code snippets.
        """
        return f"# Generated code for: {requirements}\n# Implementation goes here"
    
    def _create_agent(self):
        """
        Create the agent with prompt template.
        """
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="""You are a helpful AI assistant with multiple capabilities.
            Use the available tools to help users with their requests.
            Always be accurate and provide detailed explanations.
            """),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        return create_openai_functions_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )
    
    def run(self, query: str) -> str:
        """
        Execute agent with user query.
        """
        try:
            logger.info(f"Processing query: {query}")
            response = self.agent_executor.invoke({"input": query})
            return response["output"]
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            return f"I encountered an error: {str(e)}"
    
    def clear_memory(self):
        """
        Clear conversation memory.
        """
        self.memory.clear()
        logger.info("Memory cleared")


if __name__ == "__main__":
    # Example usage
    agent = AIAgent()
    
    # Test queries
    print(agent.run("Calculate 25 * 4 + 10"))
    print(agent.run("Analyze this text: Hello world from AI agent"))
