# Code Analysis Patterns

## Overview

This document describes the analysis patterns and methodologies used by the code analyzer skill. These patterns are tool-agnostic and can be implemented with various code analysis tools.

## Analysis Categories

### Pattern Detection

#### Authentication & Authorization
- **Authentication Flows**: Login processes, session management, token handling
- **Access Control**: Role-based permissions, authorization checks, security policies
- **Security Patterns**: Input validation, data protection, secure communication

#### Data Flow & State Management
- **State Management**: Data storage patterns, state updates, state sharing
- **Data Flow**: Unidirectional vs bidirectional data flow, data propagation
- **Caching Strategies**: Data caching, invalidation mechanisms, performance optimization

#### API & Integration Patterns
- **API Design**: REST, GraphQL, RPC patterns and implementations
- **Integration Patterns**: Service communication, message passing, event handling
- **Error Handling**: Exception patterns, error propagation, recovery mechanisms

#### Component & Module Patterns
- **Component Composition**: Parent-child relationships, component hierarchies
- **Module Organization**: Code organization, dependency management, interface design
- **Reusable Patterns**: Abstraction levels, design patterns, code reuse

### Architecture Analysis

#### System Architecture
- **Architectural Styles**: Monolithic, microservices, layered, event-driven
- **Service Boundaries**: Module boundaries, service interfaces, integration points
- **Design Decisions**: Technology choices, architectural trade-offs, scalability considerations

#### Data Architecture
- **Data Models**: Database schemas, data relationships, normalization
- **Data Access**: ORM patterns, query optimization, transaction management
- **Data Flow**: Data pipelines, ETL processes, data transformation

#### Integration Architecture
- **External Services**: Third-party integrations, API consumption
- **Message Systems**: Message brokers, event processing, pub-sub patterns
- **Protocols**: Communication protocols, data serialization, network patterns

### Quality Assessment

#### Performance Analysis
- **Performance Patterns**: Bottlenecks, optimization opportunities, resource usage
- **Scalability**: Horizontal vs vertical scaling, load distribution
- **Efficiency**: Algorithm complexity, memory usage, I/O optimization

#### Security Assessment
- **Security Vulnerabilities**: Common vulnerabilities, security anti-patterns
- **Data Protection**: Encryption, secure storage, data privacy
- **Access Control**: Authentication weaknesses, authorization gaps

#### Code Quality
- **Maintainability**: Code complexity, coupling, cohesion
- **Readability**: Code organization, naming conventions, documentation
- **Consistency**: Coding standards, pattern consistency, style adherence

### Code Review Scenarios

#### Systematic Code Review
- **Code Quality Review**: Identify code smells, anti-patterns, improvement areas
- **Best Practices**: Check adherence to language/framework best practices
- **Technical Debt**: Identify areas needing refactoring or improvement

#### Security Review
- **Security Audit**: Identify potential security vulnerabilities
- **Data Handling**: Review data validation, sanitization, and protection
- **Access Control**: Verify authentication and authorization implementations

#### Performance Review
- **Performance Audit**: Identify performance bottlenecks and optimization opportunities
- **Resource Usage**: Analyze memory, CPU, and I/O usage patterns
- **Scalability**: Assess scalability limitations and improvement areas

#### Architecture Review
- **Design Review**: Evaluate architectural decisions and patterns
- **Integration Review**: Check service boundaries and integration points
- **Technology Review**: Assess technology choices and their implications

### Technology Audit

#### Dependency Analysis
- **Third-party Libraries**: Usage patterns, integration quality, version management
- **Security Assessment**: Known vulnerabilities, security compliance
- **Maintenance**: Update frequency, community support, long-term viability

#### Testing Strategy
- **Test Coverage**: Unit, integration, and end-to-end testing coverage
- **Testing Patterns**: Mocking strategies, test organization, quality gates
- **Test Quality**: Test maintainability, readability, effectiveness

#### Migration Readiness
- **Technology Stack**: Current technology assessment, migration feasibility
- **Dependencies**: Dependency compatibility, upgrade paths
- **Code Quality**: Code health, refactoring needs, migration complexity

### Feature Analysis

#### Feature Tracing
- **Implementation Tracing**: Track feature implementation across files and components
- **Data Flow Analysis**: Follow data flow through the system for specific features
- **Integration Points**: Identify how features integrate with other system components

#### API Analysis
- **Endpoint Cataloging**: Comprehensive API endpoint discovery and documentation
- **Request/Response Patterns**: Analyze API communication patterns and data formats
- **Authentication Requirements**: Document security requirements for each endpoint

#### Framework-Specific Analysis
- **React Hooks**: Analyze hooks usage patterns, custom hooks, and best practices
- **Database Queries**: Identify query patterns, ORM usage, and connection management
- **Component Patterns**: Framework-specific component organization and reuse

### Documentation Generation

#### Onboarding Documentation
- **Key Concepts**: Identify fundamental concepts developers need to understand
- **System Overview**: Provide high-level system architecture and component relationships
- **Setup Requirements**: Document development environment setup and dependencies

#### Technical Documentation
- **Architecture Documentation**: Generate comprehensive system architecture docs
- **API Reference**: Create detailed API documentation with examples
- **Codebase Navigation**: Help developers navigate complex codebases effectively

## Analysis Methodology

### Comprehensive Analysis
- Use `--all-files` equivalent for complete codebase coverage
- Focus on patterns rather than individual implementations
- Identify architectural decisions and their implications

### Non-Destructive Analysis
- Use safe analysis modes that don't modify code
- Focus on insights and recommendations
- Provide actionable feedback

### Context-Aware Analysis
- Consider the project's domain and requirements
- Evaluate patterns in the context of project goals
- Provide domain-specific insights

## Best Practices

### Analysis Scope
- Start with high-level architecture before diving into details
- Focus on patterns that impact maintainability and scalability
- Consider both current state and future evolution

### Result Interpretation
- Look for patterns rather than individual issues
- Consider the trade-offs in architectural decisions
- Provide context-aware recommendations

### Tool Selection
- Choose analysis tools based on project requirements
- Consider tool capabilities and limitations
- Use multiple tools for comprehensive coverage