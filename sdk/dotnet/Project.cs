// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Vercel
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Vercel = Pulumiverse.Vercel;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // A project that is connected to a git repository.
    ///     // Deployments will be created automatically
    ///     // on every branch push and merges onto the Production Branch.
    ///     var withGit = new Vercel.Project("withGit", new()
    ///     {
    ///         Framework = "nextjs",
    ///         GitRepository = new Vercel.Inputs.ProjectGitRepositoryArgs
    ///         {
    ///             Repo = "vercel/some-repo",
    ///             Type = "github",
    ///         },
    ///     });
    /// 
    ///     // A project that is not connected to a git repository.
    ///     // Deployments will need to be created manually through
    ///     // terraform, or via the vercel CLI.
    ///     var example = new Vercel.Project("example", new()
    ///     {
    ///         Framework = "nextjs",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// If importing into a personal account, or with a team configured on
    /// 
    ///  the provider, simply use the project ID.
    /// 
    ///  - project_id can be found in the project `settings` tab in the Vercel UI.
    /// 
    /// ```sh
    /// $ pulumi import vercel:index/project:Project example prj_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
    /// ```
    /// 
    ///  Alternatively, you can import via the team_id and project_id.
    /// 
    ///  - team_id can be found in the team `settings` tab in the Vercel UI.
    /// 
    ///  - project_id can be found in the project `settings` tab in the Vercel UI.
    /// 
    /// ```sh
    /// $ pulumi import vercel:index/project:Project example team_xxxxxxxxxxxxxxxxxxxxxxxx/prj_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
    /// ```
    /// </summary>
    [VercelResourceType("vercel:index/project:Project")]
    public partial class Project : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The build command for this project. If omitted, this value will be automatically detected.
        /// </summary>
        [Output("buildCommand")]
        public Output<string?> BuildCommand { get; private set; } = null!;

        /// <summary>
        /// The dev command for this project. If omitted, this value will be automatically detected.
        /// </summary>
        [Output("devCommand")]
        public Output<string?> DevCommand { get; private set; } = null!;

        /// <summary>
        /// A set of Environment Variables that should be configured for the project.
        /// </summary>
        [Output("environments")]
        public Output<ImmutableArray<Outputs.ProjectEnvironment>> Environments { get; private set; } = null!;

        /// <summary>
        /// The framework that is being used for this project. If omitted, no framework is selected.
        /// </summary>
        [Output("framework")]
        public Output<string?> Framework { get; private set; } = null!;

        /// <summary>
        /// The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected Git Repository will be automatically deployed. This requires the corresponding Vercel for [Github](https://vercel.com/docs/concepts/git/vercel-for-github), [Gitlab](https://vercel.com/docs/concepts/git/vercel-for-gitlab) or [Bitbucket](https://vercel.com/docs/concepts/git/vercel-for-bitbucket) plugins to be installed.
        /// </summary>
        [Output("gitRepository")]
        public Output<Outputs.ProjectGitRepository?> GitRepository { get; private set; } = null!;

        /// <summary>
        /// When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build has to be issued. If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a command that exits with code 1 (new Build needed) or code 0.
        /// </summary>
        [Output("ignoreCommand")]
        public Output<string?> IgnoreCommand { get; private set; } = null!;

        /// <summary>
        /// The install command for this project. If omitted, this value will be automatically detected.
        /// </summary>
        [Output("installCommand")]
        public Output<string?> InstallCommand { get; private set; } = null!;

        /// <summary>
        /// The desired name for the project.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The output directory of the project. If omitted, this value will be automatically detected.
        /// </summary>
        [Output("outputDirectory")]
        public Output<string?> OutputDirectory { get; private set; } = null!;

        /// <summary>
        /// Ensures visitors of your Preview Deployments must enter a password in order to gain access.
        /// </summary>
        [Output("passwordProtection")]
        public Output<Outputs.ProjectPasswordProtection?> PasswordProtection { get; private set; } = null!;

        /// <summary>
        /// Allow automation services to bypass Vercel Authentication and Password Protection for both Preview and Production Deployments on this project when using an HTTP header named `x-vercel-protection-bypass` with a value of the `password_protection_for_automation_secret` field.
        /// </summary>
        [Output("protectionBypassForAutomation")]
        public Output<bool?> ProtectionBypassForAutomation { get; private set; } = null!;

        /// <summary>
        /// If `protection_bypass_for_automation` is enabled, use this value in the `x-vercel-protection-bypass` header to bypass Vercel Authentication and Password Protection for both Preview and Production Deployments.
        /// </summary>
        [Output("protectionBypassForAutomationSecret")]
        public Output<string> ProtectionBypassForAutomationSecret { get; private set; } = null!;

        /// <summary>
        /// By default, visitors to the `/_logs` and `/_src` paths of your Production and Preview Deployments must log in with Vercel (requires being a member of your team) to see the Source, Logs and Deployment Status of your project. Setting `public_source` to `true` disables this behaviour, meaning the Source, Logs and Deployment Status can be publicly viewed.
        /// </summary>
        [Output("publicSource")]
        public Output<bool?> PublicSource { get; private set; } = null!;

        /// <summary>
        /// The name of a directory or relative path to the source code of your project. If omitted, it will default to the project root.
        /// </summary>
        [Output("rootDirectory")]
        public Output<string?> RootDirectory { get; private set; } = null!;

        /// <summary>
        /// The region on Vercel's network to which your Serverless Functions are deployed. It should be close to any data source your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see [Vercel's documentation](https://vercel.com/docs/concepts/edge-network/regions) for a full list of regions.
        /// </summary>
        [Output("serverlessFunctionRegion")]
        public Output<string> ServerlessFunctionRegion { get; private set; } = null!;

        /// <summary>
        /// The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the provider.
        /// </summary>
        [Output("teamId")]
        public Output<string> TeamId { get; private set; } = null!;

        /// <summary>
        /// Ensures only visitors from an allowed IP address can access your deployment.
        /// </summary>
        [Output("trustedIps")]
        public Output<Outputs.ProjectTrustedIps?> TrustedIps { get; private set; } = null!;

        /// <summary>
        /// Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team.
        /// </summary>
        [Output("vercelAuthentication")]
        public Output<Outputs.ProjectVercelAuthentication> VercelAuthentication { get; private set; } = null!;


        /// <summary>
        /// Create a Project resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Project(string name, ProjectArgs? args = null, CustomResourceOptions? options = null)
            : base("vercel:index/project:Project", name, args ?? new ProjectArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Project(string name, Input<string> id, ProjectState? state = null, CustomResourceOptions? options = null)
            : base("vercel:index/project:Project", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Project resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Project Get(string name, Input<string> id, ProjectState? state = null, CustomResourceOptions? options = null)
        {
            return new Project(name, id, state, options);
        }
    }

    public sealed class ProjectArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The build command for this project. If omitted, this value will be automatically detected.
        /// </summary>
        [Input("buildCommand")]
        public Input<string>? BuildCommand { get; set; }

        /// <summary>
        /// The dev command for this project. If omitted, this value will be automatically detected.
        /// </summary>
        [Input("devCommand")]
        public Input<string>? DevCommand { get; set; }

        [Input("environments")]
        private InputList<Inputs.ProjectEnvironmentArgs>? _environments;

        /// <summary>
        /// A set of Environment Variables that should be configured for the project.
        /// </summary>
        public InputList<Inputs.ProjectEnvironmentArgs> Environments
        {
            get => _environments ?? (_environments = new InputList<Inputs.ProjectEnvironmentArgs>());
            set => _environments = value;
        }

        /// <summary>
        /// The framework that is being used for this project. If omitted, no framework is selected.
        /// </summary>
        [Input("framework")]
        public Input<string>? Framework { get; set; }

        /// <summary>
        /// The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected Git Repository will be automatically deployed. This requires the corresponding Vercel for [Github](https://vercel.com/docs/concepts/git/vercel-for-github), [Gitlab](https://vercel.com/docs/concepts/git/vercel-for-gitlab) or [Bitbucket](https://vercel.com/docs/concepts/git/vercel-for-bitbucket) plugins to be installed.
        /// </summary>
        [Input("gitRepository")]
        public Input<Inputs.ProjectGitRepositoryArgs>? GitRepository { get; set; }

        /// <summary>
        /// When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build has to be issued. If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a command that exits with code 1 (new Build needed) or code 0.
        /// </summary>
        [Input("ignoreCommand")]
        public Input<string>? IgnoreCommand { get; set; }

        /// <summary>
        /// The install command for this project. If omitted, this value will be automatically detected.
        /// </summary>
        [Input("installCommand")]
        public Input<string>? InstallCommand { get; set; }

        /// <summary>
        /// The desired name for the project.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The output directory of the project. If omitted, this value will be automatically detected.
        /// </summary>
        [Input("outputDirectory")]
        public Input<string>? OutputDirectory { get; set; }

        /// <summary>
        /// Ensures visitors of your Preview Deployments must enter a password in order to gain access.
        /// </summary>
        [Input("passwordProtection")]
        public Input<Inputs.ProjectPasswordProtectionArgs>? PasswordProtection { get; set; }

        /// <summary>
        /// Allow automation services to bypass Vercel Authentication and Password Protection for both Preview and Production Deployments on this project when using an HTTP header named `x-vercel-protection-bypass` with a value of the `password_protection_for_automation_secret` field.
        /// </summary>
        [Input("protectionBypassForAutomation")]
        public Input<bool>? ProtectionBypassForAutomation { get; set; }

        /// <summary>
        /// By default, visitors to the `/_logs` and `/_src` paths of your Production and Preview Deployments must log in with Vercel (requires being a member of your team) to see the Source, Logs and Deployment Status of your project. Setting `public_source` to `true` disables this behaviour, meaning the Source, Logs and Deployment Status can be publicly viewed.
        /// </summary>
        [Input("publicSource")]
        public Input<bool>? PublicSource { get; set; }

        /// <summary>
        /// The name of a directory or relative path to the source code of your project. If omitted, it will default to the project root.
        /// </summary>
        [Input("rootDirectory")]
        public Input<string>? RootDirectory { get; set; }

        /// <summary>
        /// The region on Vercel's network to which your Serverless Functions are deployed. It should be close to any data source your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see [Vercel's documentation](https://vercel.com/docs/concepts/edge-network/regions) for a full list of regions.
        /// </summary>
        [Input("serverlessFunctionRegion")]
        public Input<string>? ServerlessFunctionRegion { get; set; }

        /// <summary>
        /// The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the provider.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// Ensures only visitors from an allowed IP address can access your deployment.
        /// </summary>
        [Input("trustedIps")]
        public Input<Inputs.ProjectTrustedIpsArgs>? TrustedIps { get; set; }

        /// <summary>
        /// Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team.
        /// </summary>
        [Input("vercelAuthentication")]
        public Input<Inputs.ProjectVercelAuthenticationArgs>? VercelAuthentication { get; set; }

        public ProjectArgs()
        {
        }
        public static new ProjectArgs Empty => new ProjectArgs();
    }

    public sealed class ProjectState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The build command for this project. If omitted, this value will be automatically detected.
        /// </summary>
        [Input("buildCommand")]
        public Input<string>? BuildCommand { get; set; }

        /// <summary>
        /// The dev command for this project. If omitted, this value will be automatically detected.
        /// </summary>
        [Input("devCommand")]
        public Input<string>? DevCommand { get; set; }

        [Input("environments")]
        private InputList<Inputs.ProjectEnvironmentGetArgs>? _environments;

        /// <summary>
        /// A set of Environment Variables that should be configured for the project.
        /// </summary>
        public InputList<Inputs.ProjectEnvironmentGetArgs> Environments
        {
            get => _environments ?? (_environments = new InputList<Inputs.ProjectEnvironmentGetArgs>());
            set => _environments = value;
        }

        /// <summary>
        /// The framework that is being used for this project. If omitted, no framework is selected.
        /// </summary>
        [Input("framework")]
        public Input<string>? Framework { get; set; }

        /// <summary>
        /// The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected Git Repository will be automatically deployed. This requires the corresponding Vercel for [Github](https://vercel.com/docs/concepts/git/vercel-for-github), [Gitlab](https://vercel.com/docs/concepts/git/vercel-for-gitlab) or [Bitbucket](https://vercel.com/docs/concepts/git/vercel-for-bitbucket) plugins to be installed.
        /// </summary>
        [Input("gitRepository")]
        public Input<Inputs.ProjectGitRepositoryGetArgs>? GitRepository { get; set; }

        /// <summary>
        /// When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build has to be issued. If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a command that exits with code 1 (new Build needed) or code 0.
        /// </summary>
        [Input("ignoreCommand")]
        public Input<string>? IgnoreCommand { get; set; }

        /// <summary>
        /// The install command for this project. If omitted, this value will be automatically detected.
        /// </summary>
        [Input("installCommand")]
        public Input<string>? InstallCommand { get; set; }

        /// <summary>
        /// The desired name for the project.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The output directory of the project. If omitted, this value will be automatically detected.
        /// </summary>
        [Input("outputDirectory")]
        public Input<string>? OutputDirectory { get; set; }

        /// <summary>
        /// Ensures visitors of your Preview Deployments must enter a password in order to gain access.
        /// </summary>
        [Input("passwordProtection")]
        public Input<Inputs.ProjectPasswordProtectionGetArgs>? PasswordProtection { get; set; }

        /// <summary>
        /// Allow automation services to bypass Vercel Authentication and Password Protection for both Preview and Production Deployments on this project when using an HTTP header named `x-vercel-protection-bypass` with a value of the `password_protection_for_automation_secret` field.
        /// </summary>
        [Input("protectionBypassForAutomation")]
        public Input<bool>? ProtectionBypassForAutomation { get; set; }

        /// <summary>
        /// If `protection_bypass_for_automation` is enabled, use this value in the `x-vercel-protection-bypass` header to bypass Vercel Authentication and Password Protection for both Preview and Production Deployments.
        /// </summary>
        [Input("protectionBypassForAutomationSecret")]
        public Input<string>? ProtectionBypassForAutomationSecret { get; set; }

        /// <summary>
        /// By default, visitors to the `/_logs` and `/_src` paths of your Production and Preview Deployments must log in with Vercel (requires being a member of your team) to see the Source, Logs and Deployment Status of your project. Setting `public_source` to `true` disables this behaviour, meaning the Source, Logs and Deployment Status can be publicly viewed.
        /// </summary>
        [Input("publicSource")]
        public Input<bool>? PublicSource { get; set; }

        /// <summary>
        /// The name of a directory or relative path to the source code of your project. If omitted, it will default to the project root.
        /// </summary>
        [Input("rootDirectory")]
        public Input<string>? RootDirectory { get; set; }

        /// <summary>
        /// The region on Vercel's network to which your Serverless Functions are deployed. It should be close to any data source your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see [Vercel's documentation](https://vercel.com/docs/concepts/edge-network/regions) for a full list of regions.
        /// </summary>
        [Input("serverlessFunctionRegion")]
        public Input<string>? ServerlessFunctionRegion { get; set; }

        /// <summary>
        /// The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the provider.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// Ensures only visitors from an allowed IP address can access your deployment.
        /// </summary>
        [Input("trustedIps")]
        public Input<Inputs.ProjectTrustedIpsGetArgs>? TrustedIps { get; set; }

        /// <summary>
        /// Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team.
        /// </summary>
        [Input("vercelAuthentication")]
        public Input<Inputs.ProjectVercelAuthenticationGetArgs>? VercelAuthentication { get; set; }

        public ProjectState()
        {
        }
        public static new ProjectState Empty => new ProjectState();
    }
}
