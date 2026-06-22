import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../../hooks/useAuth'

export default function Navbar() {
  const { user, signOut } = useAuth()
  const navigate = useNavigate()

  const handleSignOut = async () => {
    await signOut()
    navigate('/login')
  }

  return (
    <nav style={styles.nav}>
      <Link to="/dashboard" style={styles.brand}>
        Omni Biosystems
      </Link>
      {user && (
        <div style={styles.links}>
          <Link to="/dashboard" style={styles.link}>Dashboard</Link>
          <Link to="/profile" style={styles.link}>Profile</Link>
          <button onClick={handleSignOut} style={styles.signOut}>Sign Out</button>
        </div>
      )}
    </nav>
  )
}

const styles: Record<string, React.CSSProperties> = {
  nav: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: '0.75rem 2rem',
    background: 'var(--color-surface)',
    borderBottom: '1px solid var(--color-border)',
    boxShadow: 'var(--shadow)',
  },
  brand: { fontWeight: 700, fontSize: '1.125rem', color: 'var(--color-text)' },
  links: { display: 'flex', gap: '1.5rem', alignItems: 'center' },
  link: { color: 'var(--color-muted)', fontSize: '0.9rem' },
  signOut: {
    background: 'none',
    border: '1px solid var(--color-border)',
    borderRadius: 'var(--radius)',
    padding: '0.375rem 0.75rem',
    fontSize: '0.875rem',
    color: 'var(--color-muted)',
  },
}
