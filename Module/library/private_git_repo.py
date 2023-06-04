from github import Github
from ansible.module_utils.basic import AnsibleModule
# import requests

def main():
    fields= {
            "github_token": {"required": True, "type": "str"},
            "repo_username": {"required": True, "type": "str"},
            "repo_name": {"required": True, "type": "str"},
            "repo_file_path": {"required": True, "type": "str"},
            "repo_branch": {"required": True, "type": "str"},
            "save_file_path": {"required": True, "type": "str"}
            }
    module = AnsibleModule(argument_spec=fields)
    gt = module.params['github_token']
    ru = module.params['repo_username']
    rn = module.params['repo_name']
    rfp = module.params['repo_file_path'] #Must include file_name
    br = module.params['repo_branch']
    sfp = module.params['save_file_path']
    g = Github(gt)
    try:
        repo = g.get_repo(f'{ru}/{rn}')
        file_contents = repo.get_contents(f'{rfp}')

        file_content = file_contents.decoded_content
        with open(sfp, 'wb') as file:
            file.write(file_content)

        module.exit_json(changed=True, msg='File Downloaded Successfully')
    except Exception as e:
        module.fail_json(msg='Ansibl Module Encountered a Failure')

if __name__ == '__main__':
    main()