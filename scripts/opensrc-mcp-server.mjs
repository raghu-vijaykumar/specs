import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import * as z from 'zod';
import { execSync } from 'child_process';

const server = new McpServer({
  name: 'opensrc',
  version: '1.0.0',
});

server.tool(
  'opensrc_path',
  'Get the absolute path to a package\'s source code (fetches on cache miss). Use this to then read files. Supports npm (default), pypi:, crates:, and owner/repo.',
  {
    pkg: z.string().describe('Package name (e.g. zod, pypi:requests, crates:serde, facebook/react)'),
    version: z.string().optional().describe('Optional version (e.g. 3.22.0, @v1.0.0, #main)'),
    cwd: z.string().optional().describe('Working directory for lockfile version resolution'),
  },
  async ({ pkg, version, cwd }) => {
    const pkgSpec = pkg + (version ? (version.startsWith('@') || version.startsWith('#') ? version : `@${version}`) : '');
    const cwdFlag = cwd ? ` --cwd "${cwd}"` : '';
    const result = execSync(`opensrc path "${pkgSpec}"${cwdFlag}`, { encoding: 'utf-8', timeout: 60000 }).trim();
    return { content: [{ type: 'text', text: result }] };
  }
);

server.tool(
  'opensrc_fetch',
  'Pre-fetch one or more packages into the cache without printing paths.',
  {
    packages: z.array(z.string()).describe('One or more package specifiers'),
  },
  async ({ packages }) => {
    const result = execSync(`opensrc fetch ${packages.join(' ')}`, { encoding: 'utf-8', timeout: 120000 }).trim();
    return { content: [{ type: 'text', text: result || 'Fetch complete.' }] };
  }
);

server.tool(
  'opensrc_list',
  'List all cached source packages.',
  {
    json: z.boolean().optional().describe('Output as JSON'),
  },
  async ({ json }) => {
    const jsonFlag = json ? ' --json' : '';
    const result = execSync(`opensrc list${jsonFlag}`, { encoding: 'utf-8', timeout: 10000 }).trim();
    return { content: [{ type: 'text', text: result }] };
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
