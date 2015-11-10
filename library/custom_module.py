#!/usr/bin/python


def main():
    module = AnsibleModule(argument_spec={})
    module.exit_json(msg="Hello")


from ansible.module_utils.basic import *  # noqa

if __name__ == '__main__':
    main()
