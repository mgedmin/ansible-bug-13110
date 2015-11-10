try:
    # Ansible 2
    from ansible.plugins.action.normal import ActionModule
except ImportError:
    # Ansible 1
    from ansible.runner.action_plugins.normal import ActionModule
